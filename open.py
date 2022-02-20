def main():
    try:
        configuration=open('config.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el archivo de configuración :C")

if __name__ == '__main__':
    main()