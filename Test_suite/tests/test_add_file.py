from time import sleep

class TestAddFile:
    def test_add_file(self, browser, input_page):
        path = 'K:/Learn/POM_Learning_OTUS/Test_suite/data/pict.jpg'
        input_page.load_file(path=path)

    def test_add_file_to_opencart(self, browser, admin_product_page):
        path = 'K:/Learn/POM_Learning_OTUS/Test_suite/data/pict.jpg'
        sleep(5)



