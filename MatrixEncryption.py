number_columns = 4
sample_string = input("Şifrelemek istediğiniz metni giriniz.")
sample_string = sample_string.replace(' ', '')

l = [list(sample_string[i:i+number_columns]) for i in range(0, len(sample_string), number_columns)]
matrix = [s if len(s) == number_columns else s+["X"]*(number_columns-len(s)) for s in l]


print("{}\n{}\n{}\n{}".format(matrix[:1],matrix[1:2],matrix[2:3],matrix[3:4]))