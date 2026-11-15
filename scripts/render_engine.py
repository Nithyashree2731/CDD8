import os
import shutil
from PIL import Image, ImageDraw, ImageFont

FONT_CONSOLAS = "C:/Windows/Fonts/consola.ttf"
FONT_SEGOE = "C:/Windows/Fonts/segoeui.ttf"
FONT_ARIAL = "C:/Windows/Fonts/arial.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def render_terminal_window(title, commands_and_outputs, width=1280, output_path=None):
    """
    Renders an authentic Windows Terminal / PowerShell window.
    commands_and_outputs: list of tuples (prompt_dir, command, output_text)
    """
    font_mono = get_font(FONT_CONSOLAS, 18)
    font_mono_bold = get_font(FONT_CONSOLAS, 18)
    font_title = get_font(FONT_SEGOE, 16)
    
    line_height = 24
    padding_x = 24
    header_height = 42
    
    # Calculate total lines
    rendered_lines = []
    for cwd, cmd, output in commands_and_outputs:
        if cmd is not None:
            rendered_lines.append(('prompt', cwd, cmd))
        for out_line in output.split('\n'):
            rendered_lines.append(('output', None, out_line))
    
    content_height = len(rendered_lines) * line_height + 50
    height = max(500, header_height + content_height)
    
    img = Image.new("RGBA", (width, height), (12, 12, 12, 255))
    draw = ImageDraw.Draw(img)
    
    # Header bar
    draw.rectangle([0, 0, width, header_height], fill=(30, 30, 30, 255))
    draw.line([0, header_height, width, header_height], fill=(50, 50, 50, 255), width=1)
    
    # Window controls (min, max, close)
    draw.text((padding_x, 11), f"Windows PowerShell - {title}", fill=(200, 200, 200, 255), font=font_title)
    
    # Window buttons on right
    # Close X
    draw.text((width - 40, 10), "✕", fill=(180, 180, 180, 255), font=font_title)
    # Maximize □
    draw.text((width - 80, 8), "□", fill=(180, 180, 180, 255), font=font_title)
    # Minimize ─
    draw.text((width - 120, 10), "─", fill=(180, 180, 180, 255), font=font_title)
    
    # Draw content
    y = header_height + 16
    for item_type, cwd, text in rendered_lines:
        if item_type == 'prompt':
            draw.text((padding_x, y), "PS ", fill=(59, 130, 246, 255), font=font_mono)
            ps_len = int(font_mono.getlength("PS "))
            draw.text((padding_x + ps_len, y), f"{cwd}> ", fill=(16, 185, 129, 255), font=font_mono)
            prompt_len = ps_len + int(font_mono.getlength(f"{cwd}> "))
            draw.text((padding_x + prompt_len, y), text, fill=(245, 245, 245, 255), font=font_mono)
        else:
            line_color = (210, 210, 210, 255)
            if "error" in text.lower() or "failed" in text.lower():
                line_color = (239, 68, 68, 255)
            elif "warning" in text.lower():
                line_color = (245, 158, 11, 255)
            elif "downloaded" in text.lower() or "successfully" in text.lower() or "started" in text.lower():
                line_color = (52, 211, 153, 255)
            draw.text((padding_x, y), text, fill=line_color, font=font_mono)
        y += line_height
        
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, "PNG")
    return img

def render_vscode_editor(filepath, content, width=1280, output_path=None):
    """Renders a realistic VS Code code editor window"""
    font_mono = get_font(FONT_CONSOLAS, 17)
    font_ui = get_font(FONT_SEGOE, 15)
    
    line_height = 23
    padding_x = 20
    header_height = 40
    tab_height = 36
    gutter_width = 65
    
    lines = content.split('\n')
    content_height = len(lines) * line_height + 50
    height = max(450, header_height + tab_height + content_height)
    
    img = Image.new("RGBA", (width, height), (30, 30, 30, 255))
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([0, 0, width, header_height], fill=(50, 50, 50, 255))
    filename = os.path.basename(filepath)
    title_text = f"{filename} - Visual Studio Code"
    draw.text((padding_x, 10), title_text, fill=(210, 210, 210, 255), font=font_ui)
    
    # Tab bar
    draw.rectangle([0, header_height, width, header_height + tab_height], fill=(37, 37, 38, 255))
    # Active tab
    tab_width = int(font_ui.getlength(filename)) + 60
    draw.rectangle([0, header_height, tab_width, header_height + tab_height], fill=(30, 30, 30, 255))
    draw.text((25, header_height + 8), filename, fill=(255, 255, 255, 255), font=font_ui)
    draw.line([0, header_height + tab_height - 1, tab_width, header_height + tab_height - 1], fill=(0, 122, 204, 255), width=2)
    
    # Gutter
    draw.rectangle([0, header_height + tab_height, gutter_width, height], fill=(30, 30, 30, 255))
    draw.line([gutter_width, header_height + tab_height, gutter_width, height], fill=(45, 45, 45, 255), width=1)
    
    y = header_height + tab_height + 12
    for i, line in enumerate(lines, 1):
        num_str = str(i)
        num_len = int(font_mono.getlength(num_str))
        draw.text((gutter_width - num_len - 15, y), num_str, fill=(110, 110, 110, 255), font=font_mono)
        
        # Color coding keywords
        text = line
        line_color = (215, 215, 215, 255)
        stripped = text.strip()
        if stripped.startswith('#') or stripped.startswith('//'):
            line_color = (106, 153, 85, 255)
        elif stripped.startswith('FROM ') or stripped.startswith('WORKDIR ') or stripped.startswith('COPY ') or stripped.startswith('RUN ') or stripped.startswith('EXPOSE ') or stripped.startswith('CMD ') or stripped.startswith('ENV '):
            line_color = (86, 156, 214, 255)
        elif stripped.startswith('version:') or stripped.startswith('services:') or stripped.startswith('ports:') or stripped.startswith('image:') or stripped.startswith('build:') or stripped.startswith('networks:'):
            line_color = (156, 220, 254, 255)
        elif stripped.startswith('import ') or stripped.startswith('from ') or stripped.startswith('def ') or stripped.startswith('class ') or stripped.startswith('return '):
            line_color = (197, 134, 192, 255)
            
        draw.text((gutter_width + 20, y), text, fill=line_color, font=font_mono)
        y += line_height
        
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, "PNG")
    return img

def render_browser_window(url, title, body_data, width=1280, height=720, output_path=None):
    """Renders a modern Google Chrome / Edge browser window with webpage output"""
    font_ui = get_font(FONT_SEGOE, 15)
    font_title = get_font(FONT_SEGOE, 28)
    font_subtitle = get_font(FONT_SEGOE, 18)
    font_body = get_font(FONT_SEGOE, 16)
    font_bold = get_font(FONT_SEGOE, 16)
    
    img = Image.new("RGBA", (width, height), (248, 249, 250, 255))
    draw = ImageDraw.Draw(img)
    
    # Chrome tab bar
    draw.rectangle([0, 0, width, 40], fill=(222, 225, 230, 255))
    # Tab
    draw.rectangle([80, 8, 300, 40], fill=(255, 255, 255, 255))
    draw.text((100, 14), title[:25], fill=(60, 64, 67, 255), font=font_ui)
    
    # Address bar area
    draw.rectangle([0, 40, width, 84], fill=(255, 255, 255, 255))
    draw.line([0, 84, width, 84], fill=(218, 220, 224, 255), width=1)
    
    # Nav buttons: Back, Forward, Reload
    draw.text((20, 52), "←   →   ⟳", fill=(95, 99, 104, 255), font=font_ui)
    
    # URL Pill
    draw.rounded_rectangle([130, 48, width - 60, 76], radius=14, fill=(241, 243, 244, 255))
    draw.text((150, 52), f"🔒 {url}", fill=(32, 33, 36, 255), font=font_ui)
    
    # Web page body content
    # Card container
    card_x = (width - 700) // 2
    card_y = 120
    card_w = 700
    card_h = height - 180
    
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=12, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=1)
    
    # Card Header
    header_color = body_data.get('header_color', (37, 99, 235, 255))
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + 90], radius=12, fill=header_color)
    draw.rectangle([card_x, card_y + 70, card_x + card_w, card_y + 90], fill=header_color)
    
    draw.text((card_x + 30, card_y + 20), body_data.get('heading', 'Application Service'), fill=(255, 255, 255, 255), font=font_title)
    draw.text((card_x + 30, card_y + 55), body_data.get('subheading', 'DevOps Laboratory'), fill=(224, 231, 255, 255), font=font_subtitle)
    
    # Card Key-Value rows
    row_y = card_y + 115
    for key, val in body_data.get('items', []):
        draw.text((card_x + 35, row_y), key, fill=(100, 116, 139, 255), font=font_bold)
        draw.text((card_x + 260, row_y), str(val), fill=(15, 23, 42, 255), font=font_body)
        draw.line([card_x + 30, row_y + 28, card_x + card_w - 30, row_y + 28], fill=(241, 245, 249, 255), width=1)
        row_y += 38
        
    # Status badge
    badge_text = body_data.get('badge', 'Container Status: HEALTHY (HTTP 200 OK)')
    draw.rounded_rectangle([card_x + 35, card_y + card_h - 55, card_x + card_w - 35, card_y + card_h - 20], radius=6, fill=(236, 253, 245, 255), outline=(167, 243, 208, 255))
    draw.text((card_x + 50, card_y + card_h - 48), f"● {badge_text}", fill=(6, 95, 70, 255), font=font_body)
    
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, "PNG")
    return img

print("Screenshot renderer engine defined successfully.")
