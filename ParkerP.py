def totalByYear(in_filename, year):
    fin = open(in_filename, "r", encoding ="utf-8")
    header = fin.readline()
    total=0
    for one_line in fin:
        data = one_line.split(",")
        movieYear = int(data[7])
        gross= int(data[2])
        if movieYear == year:
            total = total + gross
    print("total for " + str(year) + " =" + str(total))
    return total
    fin.close()
    
def changeByYear(in_filename, year):
    fin = open(in_filename, "r", encoding ="utf-8")
    header = fin.readline()
    total = 0
    data = one_line.split(",")
    movieYear = int(data[7])
    gross= int(data[2])
    
    
def printYears(in_filename, out_filename):
    fin = open(in_filename, "r", encoding ="utf-8")
    fout = open(out_filename, "w", encoding="utf-8")
    header = fin.readline()
    fout.write("Year")
    fout.write(",")
    fout.write("Total Revenue")
    fout.write(",")
    fout.write("Change from previous year \n")
    for yearCol in range(1939, 2024):
        total = totalByYear(in_filename, yearCol)
        prevTotal = totalByYear(in_filename, (yearCol -1))
        fout.write(str(yearCol))
        fout.write(",")
        fout.write(str(total))
        fout.write(",")
        
        if prevTotal ==0:
            change = "NA"
        elif total ==0:
            change = "NA"
        else:
            change = (total-prevTotal) / prevTotal

        fout.write(str(change))
        fout.write("\n")
    
    fin.close()
    fout.close()
    
