class Editor:
    def view_document(self):
        print("Просмотр документов доступен")

    def edit_document(self):
        print("Редактирование документов недоступно для бесплатной версии")


class ProEditor(Editor):
    def edit_document(self):
        print("Редактирование документов разрешено")


key = input("Введите ключ: ")
if len(key) < 7:
    pro_editor = ProEditor()
    pro_editor.view_document()
    pro_editor.edit_document()
else:
    editor = Editor()
    editor.view_document()
    editor.edit_document()
