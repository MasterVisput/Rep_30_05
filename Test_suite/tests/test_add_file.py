class TestAddFile:
    # решение части 1
    def test_add_file(self,input_page):
        path = 'K:/Learn/POM_Learning_OTUS/Test_suite/data/pict.jpg'
        input_page.load_file(path=path)

    # здесь будет решения части 2, когда я пойму как это сделать
    # def test_add_file_to_opencart(self, admin_product_page, setup_product_page):
    #     path = 'K:/Learn/POM_Learning_OTUS/Test_suite/data/pict.jpg'
    #     admin_product_page.add_image_to_product_by_name(p_name='Mouse', path=path)



