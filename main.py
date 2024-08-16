from app.vat import calculate_vat

def main():
    print(calculate_vat(float(input('Amount:\n')), float(input('VAT %:\n'))))

if __name__ == '__main__':
    main()
    