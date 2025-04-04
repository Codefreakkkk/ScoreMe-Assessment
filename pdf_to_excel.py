import pandas as pd

def pdf_to_excel(pdf_path, output_file):
    try:
        text_content = []
        with open(pdf_path, 'rb') as f:
            for line in f:
                try:
                    text_content.append(line.decode('utf-8').strip())
                except:
                    continue

        table_data = []
        for line in text_content:
            if any(x in line for x in ['Date', 'Transaction', 'Amount']):
                parts = line.split()
                if len(parts) >= 3:
                    table_data.append(parts[:3])

        if table_data:
            df = pd.DataFrame(table_data)
            df.to_excel(output_file, index=False, header=False)
        else:
            pd.DataFrame(columns=['Date','Transaction','Amount']).to_excel(output_file)

    except Exception as e:
        pd.DataFrame({'Status':['Processing error']}).to_excel(output_file)

pdf_to_excel('input.pdf', 'output.xlsx')
