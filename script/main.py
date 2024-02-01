import requests
from bs4 import BeautifulSoup

def get_pins_from_board(board_url):
    response = requests.get(board_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Используем более точный селектор для элементов <a> с пинами
        pin_elements = soup.select('a[href^="/pin/"]')

        pin_data = []
        for element in pin_elements:
            pin_id = element['href'].split('/')[-2]  # Извлекаем номер пина из URL
            img_element = element.find('img')

            # Используем get для безопасного доступа к атрибуту 'src'
            img_src = img_element.get('src', '').replace("236x", "originals") if img_element else None

            if pin_id and img_src:
                pin_data.append((pin_id, img_src))

        return pin_data
    else:
        print(f"Не удалось получить доступ к доске. Код состояния: {response.status_code}")
        return None

def main():
    board_url = 'https://www.pinterest.com/thisuliti/%2B/'
    
    pin_data = get_pins_from_board(board_url)

    if pin_data:
        print(f"Всего пинов: {len(pin_data)}")
        print("Номер пина - Ссылка на изображение:")
        for pin_id, img_src in pin_data:
            print(f"{pin_id} - {img_src}")
    else:
        print("Не удалось получить информацию о пинах.")

if __name__ == "__main__":
    main()
