import os

def main():
    username = os.getenv('USERNAME')
    language = os.getenv('LANGUAGE')
    print(f'the favorite language of {username} is {language}')

if __name__ == '__main__':
    main()