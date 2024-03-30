from csv import reader
import csv
import datetime
import re
outf = open('C:\\Documents\\HAMSCIData\\WSPR data\\WSPR2022v3-control\\Mar30.csv','at', newline='')
write=csv.writer(outf)
indir = 'C:\\Documents\\HAMSCIData\\WSPR data\\WSPR2022v3-control\\'
infile = indir+"2022-03-30_WSPR.csv"
legal_gridsquares = ["CN","CM","DN","DL","DM","EN","EM","EL","FN","FM","FL"]
print(infile)
with open(infile,'r') as WSPRfile:
            WSPRcsv = reader(WSPRfile)
            for row in WSPRcsv:
                Tgrid = row[2][0:4]
                Rgrid = row[7][0:4]
                Tgridpre = Tgrid[0:2]
                Rgridpre = Rgrid[0:2]
                if Tgridpre in  legal_gridsquares:
                    if Rgridpre in legal_gridsquares:
                        row.append(Tgrid)
                        row.append(Rgrid)
                        row=list(filter(None,row))
                        write.writerow(row)
WSPRfile.close()
outf.close()
print("Done")
