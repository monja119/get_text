import xlsxwriter


class Excel:
    def __init__(self, data, name):
        # initialization
        workbook = xlsxwriter.Workbook('{}.xlsx'.format(name))
        worksheet = workbook.add_worksheet()

        # writing data
        print("> Writing Data on Excel file : {}.xlsx ...".format(name))
        for k in range(len(data)):
            text, col, row = data[k]['text'],  data[k]['col'], data[k]['row']
            worksheet.write(row, col, text)

        workbook.close()
        print("> Success {}.xlsx".format(name))
