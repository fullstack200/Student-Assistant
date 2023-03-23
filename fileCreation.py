import os
from csv import writer
fileNames = ["s_bca_tt.csv","t_bca_tt.csv","f_bcaana_tt.csv","s_bcaana_tt.csv","t_bcaana_tt.csv","f_bsc(pmcs)_tt.csv","s_bsc(pmcs)_tt.csv","t_bsc(pmcs)_tt.csv","f_bsc(pme)_tt.csv","s_bsc(pme)_tt.csv","t_bsc(pme)_tt.csv","s_bba_tt.csv","t_bba_tt.csv","f_bbaava_tt.csv","s_bbaava_tt.csv","t_bbaava_tt.csv","f_bcom_tt.csv","s_bcom_tt.csv","t_bcom_tt.csv","f_bcomfin_tt.csv","s_bcomfin_tt.csv","t_bcomfin_tt.csv","f_bcomtou_tt.csv","s_bcomtou_tt.csv","t_bcomtou_tt.csv","f_baeng_tt.csv","s_baeng_tt.csv","t_baeng_tt.csv","f_basoc_tt.csv","s_basoc_tt.csv","t_basoc_tt.csv","f_baeco_tt.csv","s_baeco_tt.csv","_baeco_tt.csv"]
columns = ["Exam_Code","Exam_Name","Exam_Type","Exam_Date","Exam Duration","Marks"]
for i in fileNames:
    with open(i, 'a') as fp:
        wr = writer(fp)
        wr.writerow(columns)
        fp.close()