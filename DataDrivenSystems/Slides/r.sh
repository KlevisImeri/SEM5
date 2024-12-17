for file in *.pdf; do
  ocrmypdf -l eng --redo-ocr "$file" "$file"
done
