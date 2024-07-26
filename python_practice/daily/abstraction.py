class welcome_kit:
    provider = 'SSAFY'
    components_list = []

    def __init__(self, name):
        self.name = name
        print(f'Welcome to {self.provider}, {name}')
    
    @classmethod
    def components(cls, item):
        cls.item = item
        cls.components_list.append(item)

    @classmethod
    def print_list(cls):
        print(f'현재 수령한 물품은 총 {len(cls.components_list)}개 입니다.')
        print(cls.components_list)

welcome_kit('김승우')
item1 = welcome_kit.components('텀블러')
item2 = welcome_kit.components('집업 후드')
item3 = welcome_kit.components('티셔츠')
item4 = welcome_kit.components('다이어리')
item5 = welcome_kit.components('마우스패드')

welcome_kit.print_list()