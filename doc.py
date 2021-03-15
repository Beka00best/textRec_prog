from docx import Document
from docx.shared import RGBColor
document = Document()
p = document.add_paragraph()
ocr = 'Privet how are you'
text = 'Privat hoh tre iou'
step = max(len(text), len(ocr))
for i in range(step):
  run = p.add_run(ocr[i])
  if ocr[i] == text[i]:
    run.font.color.rgb = RGBColor(0, 255, 0)
  else:
    run.font.color.rgb = RGBColor(255, 0, 0)

document.save('demo1.docx')