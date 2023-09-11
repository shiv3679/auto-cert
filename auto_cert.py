import os
from subprocess import run

# Function to generate LaTeX code for a certificate
def generate_latex_code(name, role):
    latex_code = f"""
\\documentclass[12pt]{{article}}
\\usepackage{{graphicx}}
\\usepackage[a4paper, margin=1in]{{geometry}}
\\usepackage{{fontspec}}
\\usepackage{{fancybox}}

\\newfontfamily{{\\bebasneue}}{{BebasNeue-Regular.ttf}}
\\newfontfamily{{\\courgette}}{{Courgette-Regular.ttf}}
\\newfontfamily{{\\francois}}{{FrancoisOne-Regular.ttf}}

\\begin{{document}}
\\pagestyle{{empty}}

% Solid border
\\doublebox{{
\\begin{{minipage}}{{\\dimexpr\\textwidth-2\\fboxrule-2\\fboxsep}}
\\begin{{center}}

\\vspace{{1cm}}  % Margin at the top

% Institution name
\\parbox[c]{{\\textwidth}}{{\\centering \\baselineskip=1.5em \\bebasneue \\LARGE \\textbf{{INDIAN INSTITUTE OF SCIENCE EDUCATION AND \\\\ RESEARCH, MOHALI}}}}


\\hrulefill \\\\
\\vspace{{1cm}}

% Logo at the top
\\includegraphics[width=0.2\\textwidth]{{assets/IISER-Mohali_Logo.png}}
\\vspace{{1cm}}

% Certificate title
{{\\bebasneue \\Huge \\textbf{{CERTIFICATE}}}} \\\\
\\vspace{{1cm}}

% Certify text
{{\\courgette \\Large This certificate is proudly presented to}} \\\\
\\vspace{{1cm}}

% Name placeholder
{{\\bebasneue \\Huge \\textbf{{{{{name}}}}}}} \\\\
\\vspace{{1cm}}

% Additional text
{{\\courgette \\normalsize in recognition of their invaluable service as {role}. Their significant contributions were instrumental to the success of the 16th Foundation Day celebrations at the IISER, Mohali.}} \\\\
\\vspace{{1.5cm}}

% Signatures
\\begin{{minipage}}{{.45\\textwidth}}
  \\centering
  \\includegraphics[width=0.2\\textwidth]{{assets/Oprah-Winfrey-Signature-1.png}} \\\\
  \\hrulefill \\\\
  {{\\bebasneue \\small Dean IRO}}
\\end{{minipage}}
\\hfill
\\begin{{minipage}}{{.45\\textwidth}}
  \\centering
  \\includegraphics[width=0.2\\textwidth]{{assets/Oprah-Winfrey-Signature-1.png}} \\\\
  \\hrulefill \\\\
  {{\\bebasneue \\small Faculty Coordinator}}
\\end{{minipage}}

\\vspace{{1cm}}  % Margin after the signatures

\\end{{center}}
\\end{{minipage}}
}}

\\end{{document}}
"""
    return latex_code

# Names and roles
names = ["Dhwani Shah", "Shiv Shankar Singh", "Ritam Das"]
role = "Student Head"

# Create a certificates folder if it doesn't exist
if not os.path.exists('certificates'):
    os.makedirs('certificates')

# Generate LaTeX files and PDFs for each name
for name in names:
    # Generate LaTeX code
    latex_code = generate_latex_code(name, role)
    
    # Save the LaTeX code to a .tex file
    tex_file_path = f'certificates/certificate_{name.replace(" ", "_")}.tex'
    with open(tex_file_path, 'w') as f:
        f.write(latex_code)
    
    # Compile the LaTeX file to PDF using xelatex
    run(["xelatex", "-output-directory=certificates", tex_file_path])

print("PDF certificates have been generated and saved in the 'certificates' folder.")
