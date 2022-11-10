
# analyse of text
            result = text.split('\n')

            for k in range(len(result)):
                splitter = result[k].split('\t')
                text = splitter[11]
                col = int(splitter[2])
                row = ((int(splitter[7]) - 7) // 20) + (15 * i)  # formula of the row

                if data_ready[-1]['row'] == row and data_ready[-1]['col'] == col:
                    data_ready[-1]['text'] += " {}".format(text)
                else:
                    data_ready.append({
                        'text': text,
                        'row': row,
                        'col': col - 1
                    })
        print()
        # for k in range(len(data_ready)):
        #    print(data_ready[k])
        # Excel(data_ready, name)