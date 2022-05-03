import pandas as pd

def txt_file(file_name):
    # Extract
    f = open(file_name, "r", encoding='utf-8')
    s = f.read()
    f.close()

    # Transform
    s = s.replace("Счет ", "")

    # Load
    f = open("additional/10_file_out.txt", "w", encoding='utf-8')
    f.write(s)
    f.close()
    print(s)

def csv_file(file_name):
    # Extract
    df = pd.read_csv(file_name, sep = ';')
    count = df[df.columns[1]].count()

    # Transform
    for i in range(count):
        df.iat[i,1] = df.iat[i,1].replace("Сделка по заявке ", "")

    # Write
    df.to_csv("additional/10_Invoices_output.csv", sep=';', encoding='utf-8', index=False)
    print('Replace was successfully complete.')

def main():
    txt_file("additional/10_file_in.txt")
    csv_file("additional/10_Invoices.csv")
    return 0

if __name__ == '__main__':
    main()
