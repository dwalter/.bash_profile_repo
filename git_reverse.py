import subprocess
import re

def get_git_status():
    # Use ANSI color option to force color output
    return subprocess.check_output(['git', '-c', 'color.status=always', 'status'], universal_newlines=True)

def reorder_git_status(status):
    # Split the status into sections, preserving newlines
    sections = re.split('(\n\n)', status)

    # Initialize variables for each section
    branch_line = ""
    untracked_files = ""
    changes_not_staged = ""
    other_sections = []

    # Process each section
    current_section = ""
    for section in sections:
        current_section += section
        if section == '\n\n':
            if current_section.lstrip().startswith("\033[1m\033[31mOn branch"):  # ANSI color for "On branch"
                branch_line = current_section
            elif "Untracked files:" in current_section:
                untracked_files = current_section
            elif "Changes not staged for commit:" in current_section:
                changes_not_staged = current_section
            elif current_section.strip():  # Only add non-empty sections
                other_sections.append(current_section)
            current_section = ""

    # Add any remaining content
    if current_section.strip():
        other_sections.append(current_section)

    # Combine sections in the desired order
    reordered_status = "".join([
        branch_line,
        untracked_files,
        changes_not_staged
    ] + other_sections)

    return reordered_status

def main():
    status = get_git_status()
    reordered = reorder_git_status(status)
    print(reordered, end='')  # end='' to avoid adding an extra newline

if __name__ == "__main__":
    main()
