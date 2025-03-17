import os
import argparse
import json
from typing import Dict, List
from PyPDF2 import PdfReader, PdfWriter


def split_pdf_by_manual_chapters(input_pdf_path: str, chapters_info: List[Dict], output_dir: str = None):
    """
    根据手动指定的章节信息拆分PDF文件。
    
    Args:
        input_pdf_path (str): 输入PDF文件路径
        chapters_info (List[Dict]): 章节信息列表，每项包含标题和页码范围
        output_dir (str, optional): 输出目录路径
    """
    # 设置输出目录
    pdf_name = os.path.splitext(os.path.basename(input_pdf_path))[0]
    if output_dir is None:
        parent_dir = os.path.dirname(input_pdf_path)
        output_dir = os.path.join(parent_dir, f"{pdf_name}_chapters")
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取PDF文件
    pdf_reader = PdfReader(input_pdf_path)
    total_pages = len(pdf_reader.pages)
    print(f"PDF '{pdf_name}' 已加载，共 {total_pages} 页。")
    
    # 验证和调整章节信息
    valid_chapters = []
    for chapter in chapters_info:
        # 确保页码在有效范围内
        start_page = max(0, min(chapter['start_page'] - 1, total_pages - 1))
        end_page = max(0, min(chapter['end_page'] - 1, total_pages - 1))
        
        if start_page <= end_page:
            valid_chapters.append({
                'title': chapter['title'],
                'start_page': start_page,
                'end_page': end_page
            })
            print(f"章节: {chapter['title']} - 页码范围: {start_page + 1} 到 {end_page + 1} (共 {end_page - start_page + 1} 页)")
    
    if not valid_chapters:
        print("没有有效的章节信息，无法进行拆分。")
        return
    
    # 拆分PDF文件
    for idx, chapter in enumerate(valid_chapters, 1):
        # 创建新的PDF写入器
        pdf_writer = PdfWriter()
        
        # 添加章节的所有页面
        for page_num in range(chapter['start_page'], chapter['end_page'] + 1):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        
        # 创建输出文件名（替换非法字符）
        safe_title = "".join(c if c.isalnum() or c in " _-.,()[]" else "_" for c in chapter['title'])
        output_filename = f"{idx:02d}_{safe_title}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        # 写入文件
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
        
        print(f"已创建章节文件: {output_filename}")
    
    print(f"PDF拆分完成! 所有章节文件已保存到: {output_dir}")


def read_chapters_from_file(file_path: str) -> List[Dict]:
    """
    从JSON文件中读取章节信息。
    
    Args:
        file_path (str): JSON文件路径
        
    Returns:
        List[Dict]: 章节信息列表
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        chapters = json.load(f)
    
    # 验证章节信息格式
    required_keys = ['title', 'start_page', 'end_page']
    for chapter in chapters:
        if not all(key in chapter for key in required_keys):
            raise ValueError(f"章节信息格式错误: {chapter}，必须包含 {required_keys} 字段")
    
    return chapters


def interactive_create_chapters() -> List[Dict]:
    """
    交互式创建章节信息。
    
    Returns:
        List[Dict]: 章节信息列表
    """
    chapters = []
    print("请输入章节信息，每个章节需要标题、起始页码和结束页码")
    print("输入空行结束")
    
    while True:
        title = input("\n章节标题 (留空结束): ")
        if not title:
            break
        
        try:
            start_page = int(input("起始页码: "))
            end_page = int(input("结束页码: "))
            
            chapters.append({
                'title': title,
                'start_page': start_page,
                'end_page': end_page
            })
            
            print(f"已添加章节: {title} (页码: {start_page}-{end_page})")
        except ValueError:
            print("页码必须是整数，请重新输入此章节")
    
    return chapters


def save_chapters_to_file(chapters: List[Dict], output_file: str):
    """
    将章节信息保存到JSON文件。
    
    Args:
        chapters (List[Dict]): 章节信息列表
        output_file (str): 输出文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
    
    print(f"章节信息已保存到: {output_file}")


def main():
    """命令行入口函数"""
    parser = argparse.ArgumentParser(description='根据手动指定的章节信息拆分PDF文件')
    parser.add_argument('input_pdf', help='输入PDF文件路径')
    parser.add_argument('-o', '--output-dir', help='输出目录路径 (可选)')
    parser.add_argument('-c', '--chapters-file', help='章节信息JSON文件路径 (可选)')
    parser.add_argument('-s', '--save-chapters', help='保存章节信息到JSON文件 (可选)')
    
    args = parser.parse_args()
    
    # 获取章节信息
    if args.chapters_file:
        # 从文件读取章节信息
        print(f"从文件加载章节信息: {args.chapters_file}")
        chapters = read_chapters_from_file(args.chapters_file)
    else:
        # 交互式创建章节信息
        print("开始交互式创建章节信息...")
        chapters = interactive_create_chapters()
    
    if not chapters:
        print("没有章节信息，无法进行拆分。")
        return
    
    # 保存章节信息到文件（如果指定）
    if args.save_chapters and not args.chapters_file:
        save_chapters_to_file(chapters, args.save_chapters)
    
    # 拆分PDF文件
    split_pdf_by_manual_chapters(args.input_pdf, chapters, args.output_dir)


if __name__ == "__main__":
    main()
