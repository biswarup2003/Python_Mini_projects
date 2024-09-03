import pywhatkit as pw

txt="""Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation."""
print(txt)

save_path= r'C:\Users\Biswarup\Desktop\output\text1.png'
pw.text_to_handwriting(txt,save_path,[0,0,138])
print("END")