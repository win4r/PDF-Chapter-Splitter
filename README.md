# PDF Chapter Splitter

一个用于按章节拆分PDF文件的工具，支持自动和手动两种模式。适用于教科书、技术手册、电子书等文档的章节拆分，方便单独阅读和分析。

A tool for splitting PDF files by chapters, supporting both automatic and manual modes. Suitable for textbooks, technical manuals, ebooks, and other documents that need to be split by chapters for easier reading and analysis.

## 目录 | Contents

- [功能特点 | Features](#功能特点--features)
- [安装 | Installation](#安装--installation)
- [使用方法 | Usage](#使用方法--usage)
  - [自动模式 | Automatic Mode](#自动模式--automatic-mode)
  - [手动模式 | Manual Mode](#手动模式--manual-mode)
  - [使用章节配置文件 | Using Chapter Configuration File](#使用章节配置文件--using-chapter-configuration-file)
- [配置文件格式 | Configuration File Format](#配置文件格式--configuration-file-format)
- [命令行参数 | Command Line Arguments](#命令行参数--command-line-arguments)
- [示例 | Examples](#示例--examples)
- [常见问题 | FAQ](#常见问题--faq)
- [许可证 | License](#许可证--license)

## 功能特点 | Features

### 中文

- **自动模式**：尝试从PDF中提取目录信息，自动识别章节结构
  - 支持处理内置书签
  - 支持从文本内容中提取目录信息
  - 支持多种章节格式（中文和英文）
- **手动模式**：根据用户指定的章节信息进行拆分
  - 交互式输入章节信息
  - 通过JSON文件批量指定章节信息
- **智能页码处理**：自动处理PDF显示页码与实际页码之间的偏移
- **灵活的输出选项**：
  - 可以自定义输出目录
  - 文件命名格式：序号_章节名.pdf
  - 可以保存和重用章节配置信息

### English

- **Automatic Mode**: Attempts to extract table of contents information from the PDF, automatically recognizing chapter structure
  - Supports processing built-in bookmarks
  - Supports extracting table of contents information from text content
  - Supports various chapter formats (Chinese and English)
- **Manual Mode**: Splits according to user-specified chapter information
  - Interactive input of chapter information
  - Batch specification of chapter information via JSON file
- **Intelligent Page Handling**: Automatically handles offsets between PDF display page numbers and actual page numbers
- **Flexible Output Options**:
  - Customizable output directory
  - File naming format: number_chapterName.pdf
  - Can save and reuse chapter configuration information

## 安装 | Installation

### 中文

1. 确保您已安装Python 3.6或更高版本
2. 克隆此仓库：
   ```bash
   git clone https://github.com/yourusername/pdf-chapter-splitter.git
   cd pdf-chapter-splitter
   ```
3. 安装依赖：
   ```bash
   pip install PyPDF2 pdfplumber
   ```

### English

1. Ensure you have Python 3.6 or higher installed
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pdf-chapter-splitter.git
   cd pdf-chapter-splitter
   ```
3. Install dependencies:
   ```bash
   pip install PyPDF2 pdfplumber
   ```

## 使用方法 | Usage

### 自动模式 | Automatic Mode

#### 中文

自动模式尝试从PDF中提取目录信息并按章节拆分：

```bash
python pdf_splitter.py "/path/to/your/book.pdf"
```

启用调试模式以获取更详细的输出：

```bash
python pdf_splitter.py "/path/to/your/book.pdf" --debug
```

#### English

Automatic mode attempts to extract table of contents information from the PDF and split by chapters:

```bash
python pdf_splitter.py "/path/to/your/book.pdf"
```

Enable debug mode for more detailed output:

```bash
python pdf_splitter.py "/path/to/your/book.pdf" --debug
```

### 手动模式 | Manual Mode

#### 中文

手动模式允许您交互式指定章节信息：

```bash
python pdf_manual_splitter.py "/path/to/your/book.pdf"
```

程序会提示您输入每个章节的标题、起始页码和结束页码。

#### English

Manual mode allows you to interactively specify chapter information:

```bash
python pdf_manual_splitter.py "/path/to/your/book.pdf"
```

The program will prompt you to enter the title, start page, and end page for each chapter.

### 使用章节配置文件 | Using Chapter Configuration File

#### 中文

您可以从JSON文件加载章节信息：

```bash
python pdf_manual_splitter.py "/path/to/your/book.pdf" --chapters-file chapters.json
```

您也可以保存章节信息以供将来使用：

```bash
python pdf_manual_splitter.py "/path/to/your/book.pdf" --save-chapters chapters.json
```

#### English

You can load chapter information from a JSON file:

```bash
python pdf_manual_splitter.py "/path/to/your/book.pdf" --chapters-file chapters.json
```

You can also save chapter information for future use:

```bash
python pdf_manual_splitter.py "/path/to/your/book.pdf" --save-chapters chapters.json
```

## 配置文件格式 | Configuration File Format

### 中文

章节配置文件使用JSON格式，示例如下：

```json
[
  {
    "title": "第一章：介绍",
    "start_page": 1,
    "end_page": 20
  },
  {
    "title": "第二章：基础知识",
    "start_page": 21,
    "end_page": 45
  }
]
```

每个章节项必须包含以下字段：
- `title`：章节标题
- `start_page`：起始页码（PDF中显示的页码）
- `end_page`：结束页码（PDF中显示的页码）

### English

The chapter configuration file uses JSON format, as shown in the example below:

```json
[
  {
    "title": "Chapter 1: Introduction",
    "start_page": 1,
    "end_page": 20
  },
  {
    "title": "Chapter 2: Fundamentals",
    "start_page": 21,
    "end_page": 45
  }
]
```

Each chapter item must include the following fields:
- `title`: Chapter title
- `start_page`: Starting page number (as displayed in the PDF)
- `end_page`: Ending page number (as displayed in the PDF)

## 命令行参数 | Command Line Arguments

### 自动模式 | Automatic Mode

#### 中文

```
python pdf_splitter.py [-h] [-o OUTPUT_DIR] [-d] input_pdf

位置参数:
  input_pdf             输入PDF文件路径

可选参数:
  -h, --help            显示帮助信息并退出
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        输出目录路径 (可选)
  -d, --debug           启用调试模式
```

#### English

```
python pdf_splitter.py [-h] [-o OUTPUT_DIR] [-d] input_pdf

Positional arguments:
  input_pdf             Input PDF file path

Optional arguments:
  -h, --help            Show this help message and exit
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Output directory path (optional)
  -d, --debug           Enable debug mode
```

### 手动模式 | Manual Mode

#### 中文

```
python pdf_manual_splitter.py [-h] [-o OUTPUT_DIR] [-c CHAPTERS_FILE] [-s SAVE_CHAPTERS] input_pdf

位置参数:
  input_pdf             输入PDF文件路径

可选参数:
  -h, --help            显示帮助信息并退出
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        输出目录路径 (可选)
  -c CHAPTERS_FILE, --chapters-file CHAPTERS_FILE
                        章节信息JSON文件路径 (可选)
  -s SAVE_CHAPTERS, --save-chapters SAVE_CHAPTERS
                        保存章节信息到JSON文件 (可选)
```

#### English

```
python pdf_manual_splitter.py [-h] [-o OUTPUT_DIR] [-c CHAPTERS_FILE] [-s SAVE_CHAPTERS] input_pdf

Positional arguments:
  input_pdf             Input PDF file path

Optional arguments:
  -h, --help            Show this help message and exit
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Output directory path (optional)
  -c CHAPTERS_FILE, --chapters-file CHAPTERS_FILE
                        Chapter information JSON file path (optional)
  -s SAVE_CHAPTERS, --save-chapters SAVE_CHAPTERS
                        Save chapter information to JSON file (optional)
```

## 示例 | Examples

### 中文

**示例1：使用自动模式拆分PDF**

```bash
python pdf_splitter.py "技术手册.pdf"
```

**示例2：准备章节配置文件**

```json
[
  {
    "title": "1. 理解大型语言模型",
    "start_page": 1,
    "end_page": 16
  },
  {
    "title": "2. 处理文本数据",
    "start_page": 17,
    "end_page": 49
  }
]
```

**示例3：使用配置文件拆分PDF**

```bash
python pdf_manual_splitter.py "大型语言模型构建.pdf" --chapters-file llm_chapters.json --output-dir "拆分章节"
```

### English

**Example 1: Split a PDF using automatic mode**

```bash
python pdf_splitter.py "technical_manual.pdf"
```

**Example 2: Prepare a chapter configuration file**

```json
[
  {
    "title": "1. Understanding Large Language Models",
    "start_page": 1,
    "end_page": 16
  },
  {
    "title": "2. Working with Text Data",
    "start_page": 17,
    "end_page": 49
  }
]
```

**Example 3: Split a PDF using a configuration file**

```bash
python pdf_manual_splitter.py "build_llm.pdf" --chapters-file llm_chapters.json --output-dir "split_chapters"
```

## 常见问题 | FAQ

### 中文

**问：为什么自动提取的目录不准确？**

答：PDF的结构多种多样，有些PDF没有内置书签或结构化目录，有些使用非标准格式，还有些包含复杂布局。这些因素都可能导致自动提取不准确。在这种情况下，建议使用手动模式。

**问：如何处理页码偏移问题？**

答：PDF中显示的页码与实际页面索引通常不同。例如，第一章可能从PDF中的第15页开始，但显示为第1页。使用手动模式并指定正确的页码可以解决这个问题。

**问：如何快速创建章节配置文件？**

答：浏览PDF，记录每章的开始和结束页码，然后使用文本编辑器创建符合要求格式的JSON文件，或使用交互式方式创建并保存。

### English

**Q: Why is the automatically extracted table of contents inaccurate?**

A: PDFs have diverse structures. Some PDFs don't have built-in bookmarks or structured table of contents, some use non-standard formats, and others contain complex layouts. These factors can lead to inaccurate automatic extraction. In such cases, it's recommended to use manual mode.

**Q: How to handle page numbering offset issues?**

A: The page numbers displayed in a PDF often differ from the actual page indices. For example, Chapter 1 might start on page 15 of the PDF but be displayed as page 1. Using manual mode and specifying the correct page numbers can resolve this issue.

**Q: How to quickly create a chapter configuration file?**

A: Browse through the PDF, note the start and end page numbers for each chapter, then use a text editor to create a JSON file in the required format, or use the interactive mode to create and save the configuration.

## 许可证 | License

### 中文

本项目采用MIT许可证。详见 [LICENSE](LICENSE) 文件。

### English

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
