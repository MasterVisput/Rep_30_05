from time import sleep

class TestAddFile:
    def test_add_file(self,input_page):
        path = 'K:/Learn/POM_Learning_OTUS/Test_suite/data/pict.jpg'
        input_page.load_file(path=path)


