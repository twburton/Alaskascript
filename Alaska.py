
import arcpy, string, os

#import shapefile
#import json
from arcpy import env
#from time import sleep
import xlrd
from xlrd import open_workbook
#set workspace
fc= arcpy.GetParameterAsText(1) 
arcpy.env.workspace =fc
arcpy.env.overwriteOutput= True

#from bs4 import BeautifulSoup
import urllib
import csv
#import shapefile


#input data from script into variables
#shapefile boundaries
clipfeatures= arcpy.GetParameterAsText(0)
#output gdb
gdb=arcpy.GetParameterAsText(1)
#name of featureclass
featureclassname =arcpy.GetParameterAsText(2)
#path of clipped feature
outclipfeature=arcpy.GetParameterAsText(3)
#bison query string that has bounding box that encompasses park boundary ex: querystring="https://bison.usgs.gov/solr/occurrences/select/?q={!bbox pt=66.62313748,-159.341958 sfield=geo d=1}&rows=1000000&wt=json"
#https://bison.usgs.gov/solr/occurrences/select/?q={!bbox pt=60.80971555,-162.97316711 sfield=geo d=3}&rows=100&wt=json
querystring=arcpy.GetParameterAsText(4)
#querystring='https://bison.usgs.gov/solr/occurrences/select/?q={!bbox pt=60.80971555,-162.97316711 sfield=geo d=3}&rows=10000000&wt=json'
outproject=gdb+"\\reproject"


#'https://bison.usgs.gov/solr/occurrences/select/?q=decimalLatitude:[35.38%20TO%2035.87]%20AND%20decimalLongitude:[-84.058%20TO%20-82.96]&wt=json&facet=true&facet.limit=-1&facet.mincount=1&facet.pivot=kingdom,scientificName&&indent=true'






resultarray = []
response = urllib.urlopen(querystring)
#datajson = json.loads(response.read())
ur = urllib.urlopen(querystring)
queryresult = ur.read()
resultarray.append(str(queryresult))
				
#remove extra brackets
for item in resultarray:
	if item =="]" or item =="[":
		resultarray.remove(item)
resultarray=''.join(resultarray)

#goes through string to extract field data
def find_fields(s):
	count=count1=count2=count3=count4=count5=count6=count7=count8=count9=count10=count11=count12=count13=count14= count15=count16=count17=count18=count19=count20=count21=count22=count23=count24=count25=0
	mylist1,mylist2,mylist3,mylist4,mylist5,mylist6,mylist7,mylist8,mylist9,mylist10,mylist11,mylist12,mylist13,mylist14,mylist15,mylist16,mylist17,mylist18,mylist19,mylist20,mylist21,mylist22,mylist23,mylist24,mylist25 = ([] for i in range(25))
	for i in xrange(len(s)):
		if s[i]=='"':
			if s[i:i+16] == '"scientificName"':
				count1 += 1
				for j in xrange(100):
					if s[i+18+j]=='"':
						j2=j
						break
				longi =s[i+18:i+18+j2]
				mylist1.append(longi)
				continue
			if s[i:i+19] == '"decimalLongitude":':
				count2 += 1
				for j in xrange(100):
					if s[i+19+j]==',':
						j2=j
						break
				longi =s[i+19:i+19+j2]
				mylist2.append(longi)
				continue
			if s[i:i+18] == '"decimalLatitude":':
				count3 += 1
				for j in xrange(100):
					if s[i+18+j]==',':
						j2=j
						break
				lat =s[i+18:i+18+j2]
				mylist3.append(lat)
				continue
			if s[i:i+26] == '"providedScientificName":"':
				count4 += 1
				for j in xrange(100):
					if s[i+26+j]=='"':
						j2=j
						break
				data =s[i+26:i+26+j2]
				if data == "":
					data = "null"
				mylist4.append(data)
				continue
			if s[i:i+22] == '"ITISscientificName":"':
				count5 += 1
				for j in xrange(100):
					if s[i+22+j]=='"':
						j2=j
						break
				data =s[i+22:i+22+j2]
				if data == "":
					data = "null"
				mylist5.append(data)
				continue
			if s[i:i+17] == '"catalogNumber":"':
				count6 += 1
				for j in xrange(100):
					if s[i+17+j]=='"':
						j2=j
						break
				data =s[i+17:i+17+j2]
				if data == "":
					data = "null"
				mylist6.append(data)
				continue
			if s[i:i+17] == '"basisOfRecord":"':
				count7 += 1
				for j in xrange(100):
					if s[i+17+j]=='"':
						j2=j
						break
				data =s[i+17:i+17+j2]
				if data == "":
					data = "null"
				mylist7.append(data)
				continue
			if s[i:i+13] == '"eventDate":"':
				count8 += 1
				for j in xrange(100):
					if s[i+13+j]=='"':
						j2=j
						break
				data =s[i+13:i+13+j2]
				if data == "":
					data = "null"
				mylist8.append(data)
				continue
			if s[i:i+14] == '"recordedBy":"':
				count9 += 1
				for j in xrange(100):
					if s[i+14+j]=='"':
						j2=j
						break
				data =s[i+14:i+14+j2]
				if data == "":
					data = "null"
				mylist9.append(data)
				continue
			if s[i:i+13] == '"providerID":':
				count10 += 1
				for j in xrange(100):
					if s[i+13+j]==',':
						j2=j
						break
				prov =s[i+13:i+13+j2]
				if prov == "":
					prov = "null"
				mylist10.append(prov)
				continue
			if s[i:i+33] == '"coordinateUncertaintyInMeters":"': 
				count11 += 1
				for j in xrange(100):
					if s[i+33+j]=='"':
						j2=j
						break
				data =s[i+33:i+33+j2]
				if data == "":
					data = "null"
				mylist11.append(data)
				continue
			if s[i:i+22] == '"collectionID":"':
				count12 += 1
				for j in xrange(100):
					if s[i+22+j]=='"':
						j2=j
						break
				data =s[i+22:i+22+j2]
				if data == "":
					data = "null"
				mylist12.append(data)
				continue
			if s[i:i+17] == '"institutionID":"':
				count13 += 1
				for j in xrange(100):
					if s[i+17+j]=='"':
						j2=j
						break
				data =s[i+17:i+17+j2]
				if data == "":
					data = "null"
				mylist13.append(data)
				continue
			if s[i:i+21] == '"computedStateFips":"':
				count14 += 1
				for j in xrange(100):
					if s[i+21+j]=='"':
						j2=j
						break
				data =s[i+21:i+21+j2]
				if data == "":
					data = "null"
				mylist14.append(data)
				continue
			if s[i:i+11] == '"license":"':
				count15 += 1
				for j in xrange(100):
					if s[i+11+j]=='"':
						j2=j
						break
				data =s[i+11:i+11+j2]
				if data == "":
					data = "null"
				mylist15.append(data)
				continue
			if s[i:i+17] == '"geodeticDatum":"':
				count16 += 1
				for j in xrange(100):
					if s[i+17+j]==',':
						j2=j
						break
				data =s[i+17:i+17+j2]
				if data == "":
					data = "null"
				mylist16.append(data)
				continue
			if s[i:i+17] == '"stateProvince":"':
				count17 += 1
				for j in xrange(100):
					if s[i+17+j]=='"':
						j2=j
						break
				data =s[i+17:i+17+j2]
				if data == "":
					data = "null"
				mylist17.append(data)
				continue
			if s[i:i+23] == '"coordinatePrecision":"':
				count18 += 1
				for j in xrange(100):
					if s[i+23+j]=='"':
						j2=j
						break
				data =s[i+23:i+23+j2]
				if data == "":
					data = "null"
				mylist18.append(data)
				continue
			if s[i:i+7] == '"year":':
				count19 += 1
				for j in xrange(100):
					if s[i+7+j]==',':
						j2=j
						break
				year =s[i+7:i+7+j2]
				if year == "":
					year = "null"
				mylist19.append(year)
				continue
			if s[i:i+14] == '"resourceID":"':
				count20 += 1
				for j in xrange(100):
					if s[i+14+j]=='"':
						j2=j
						break
				data =s[i+14:i+14+j2]
				if data == "":
					data = "null"
				mylist20.append(data)
				continue		
			if s[i:i+18] == '"providedCounty":"':
				count21 += 1
				for j in xrange(100):
					if s[i+18+j]=='"':
						j2=j
						break
				data =s[i+18:i+18+j2]
				if data == "":
					data = "null"
				mylist21.append(data)
				continue
			if s[i:i+17] == '"providedState":"':
				count22 += 1
				for j in xrange(100):
					if s[i+17+j]=='"':
						j2=j
						break
				data =s[i+17:i+17+j2]
				if data == "":
					data = "null"
				mylist22.append(data)
				continue
			if s[i:i+19] == '"institutionCode":"':
				count23 += 1
				for j in xrange(100):
					if s[i+19+j]=='"':
						j2=j
						break
				data =s[i+19:i+19+j2]
				if data == "":
					data = "null"
				mylist23.append(data)
				continue
			if s[i:i+11] == '"bisonID":"':
				count24 += 1
				for j in xrange(100):
					if s[i+11+j]=='"':
						j2=j
						break
				data =s[i+11:i+11+j2]
				if data == "":
					data = "null"
				mylist24.append(data)
				continue
			if s[i:i+22] == '"providedCommonName":"':
				count25 += 1
				for j in xrange(100):
					if s[i+22+j]=='"':
						j2=j
						break
				data =s[i+22:i+22+j2]
				if data == "":
					data = "null"
				mylist25.append(data)
				continue
			
			

		#keeps a running count of the number of brackets read through and subtracts extraneous brackets with each header and url to keep track of occurrences
		if s[i] == "{":
			if s[i:i+18] == '{"responseHeader":':
				count-=5
			if s[i+2:i+6] == '"url':
				count-=1
				
			#if the field is missing then add a null to that field
			if (count > count1):
				mylist1.append("null")
				count1 += 1
			if (count > count2):
				mylist2.append(0)
				count2 += 1
			if (count > count3):
				mylist3.append(0)
				count3 += 1
			if (count > count4):
				#arcpy.AddMessage("county: "+str(count4))
				#arcpy.AddMessage("LONGI: "+str(count5))
				mylist4.append("null")
				count4 += 1
			if (count > count5):
				mylist5.append("null")
				count5 += 1
			if (count > count6):
				mylist6.append("null")
				count6 += 1
			if (count > count7):
				mylist7.append("null")
				count7 += 1
			if (count > count8):
				mylist8.append("null")
				count8 += 1
			if (count > count9):
				mylist9.append("null")
				count9 += 1
			if (count > count10):
				mylist10.append("null")
				count10 += 1
			if (count > count11):
				mylist11.append("null")
				count11 += 1
			if (count > count12):
				mylist12.append("null")
				count12 += 1
			if (count > count13):
				mylist13.append("null")
				count13 += 1
			if (count > count14):
				mylist14.append("null")
				count14 += 1
			if (count > count15):
				mylist15.append("null")
				count15 += 1
			if (count > count16):
				mylist16.append("null")
				count16 += 1
			if (count > count17):
				mylist17.append("null")
				count17 += 1
			if (count > count18):
				mylist18.append("null")
				count18 += 1
			if (count > count19):
				mylist19.append("null")
				count19 += 1
			if (count > count20):
				mylist20.append("null")
				count20 += 1
			if (count > count21):
				mylist21.append("null")
				count21 += 1
			if (count > count22):
				mylist22.append("null")
				count22 += 1
			if (count > count23):
				mylist23.append("null")
				count23 += 1
			if (count > count24):
				mylist24.append("null")
				count24 += 1
			if (count > count25):
				mylist25.append("null")
				count25 += 1
			
			count+=1	
			
	#covers missing fields at the end of the string	
	if (count > count1):
		mylist1.append("null")
		count1 += 1
	if (count > count2):
		mylist2.append("null")
		count2 += 1
	if (count > count3):
		mylist3.append("null")
		count3 += 1
	if (count > count4):
		mylist4.append("null")
		count4 += 1
	if (count > count5):
		mylist5.append("null")
		count5 += 1
	if (count > count6):
		mylist6.append("null")
		count6 += 1
	if (count > count7):
		mylist7.append("null")
		count7 += 1
	if (count > count8):
		mylist8.append("null")
		count8 += 1
	if (count > count9):
		mylist9.append("null")
		count9 += 1
	if (count > count10):
		mylist10.append("null")
		count10 += 1
	if (count > count11):
		mylist11.append("null")
		count11 += 1
	if (count > count12):
		mylist12.append("null")
		count12 += 1
	if (count > count13):
		mylist13.append("null")
		count13 += 1
	if (count > count14):
		mylist14.append("null")
		count14 += 1
	if (count > count15):
		mylist15.append("null")
		count15 += 1
	if (count > count16):
		mylist16.append("null")
		count16 += 1
	if (count > count17):
		mylist17.append("null")
		count17 += 1
	if (count > count18):
		mylist18.append("null")
		count18 += 1
	if (count > count19):
		mylist19.append("null")
		count19 += 1
	if (count > count20):
		mylist20.append("null")
		count20 += 1
	if (count > count21):
		mylist21.append("null")
		count21 += 1
	if (count > count22):
		mylist22.append("null")
		count22 += 1
	if (count > count23):
		mylist23.append("null")
		count23 += 1
	if (count > count24):
		mylist24.append("null")
		count24 += 1
	if (count > count25):
		mylist25.append("null")
		count25 += 1
		
	return mylist1,mylist2,mylist3,mylist4,mylist5,mylist6,mylist7,mylist8,mylist9,mylist10,mylist11,mylist12,mylist13,mylist14,mylist15,mylist16,mylist17,mylist18,mylist19,mylist20,mylist21,mylist22,mylist23,mylist24,mylist25

#put fields into separate arrays
a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=find_fields(str(resultarray))

###
###
# json_data=open(datajson)
# data2 = json.load(json_data)

# w=shapefile.Writer(shapefile.POINT)
# w.field("scientificName")
# w.field("decimalLongitude")
# w.field("decimalLatitude")
# w.field("providedScientificName")
# w.field("providedCommonName")
# w.field("ITISscientificName")
# w.field("catalogNumber")
# w.field("basisOfRecord")
# w.field("eventDate")
# w.field("recordedBy")
# w.field("providerID")
# w.field("coordinateUncertaintyInMeters")
# w.field("collectionID")
# w.field("institutionID")
# w.field("computedStateFips")
# w.field("license")
# w.field("geodeticDatum")
# w.field("stateProvince")
# w.field("coordinatePrecision")
# w.field("year")
# w.field("resourceID")
# w.field("providedCounty")
# w.field("providedState")
# w.field("institutionCode")
# w.field("bisonID")



# w.point(float(data2["fields"][i]["lng"]),float(data2["fields"][i]["lat"]))
# w.record(data2["fields"][i]["id"],data2["fields"][i]["address"],data2["fields"][i]["lat"],data2["fields"][i]["lng"],data2["fields"][i]["rate"],data2["fields"][i]["rate_half_hour"],data2["fields"][i]["carpark_type"],data2["fields"][i]["carpark_type_str"],data2["fields"][i]["max_height"],data2["fields"][i]["capacity"],data2["fields"][i]["payment_options"],data2["fields"][i]["rate_details"])
# i+=1

# prj = open("csvSHP.prj", "w")
# epsg = ‘GEOGCS["WGS 84",’
# epsg += ‘DATUM["WGS_1984",’
# epsg += ‘SPHEROID["WGS 84",6378137,298.257223563]]’
# epsg += ‘,PRIMEM["Greenwich",0],’
# epsg += ‘UNIT["degree",0.0174532925199433]]’
# prj.write(epsg)
# prj.close()

###
###


#Park id is added to feature class name
fcname="preclip"+ str(featureclassname)

#North American Datum 1983 spatial reference
sr = arcpy.SpatialReference(4324)
#sr = arcpy.Describe(clipfeatures).spatialReference
#arcpy.AddMessage(sr)
#Create feature class
arcpy.CreateFeatureclass_management(gdb,fcname, "POINT","","","",sr)
fc= os.path.join(gdb,fcname)

#Create a list of the field names
flds=["SHAPE@XY","scientificName","providedScientificName","ITISscientificName","providedCommonName","catalogNumber","basisOfRecord","eventDate","recordedBy","providerID","coordinateUncertaintyInMeters","collectionID","institutionID","computedStateFips","license","geodeticDatum","stateProvince","coordinatePrecision", "year", "resourceID","providedCounty", "providedState", "institutionCode", "bisonID"]

#Create fields
try:
	arcpy.AddField_management(fc, "scientificName","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "providedScientificName","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "ITISscientificName","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "providedCommonName","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "catalogNumber","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "basisOfRecord","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "eventDate","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "recordedBy","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "providerID","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "coordinateUncertaintyInMeters","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "collectionID","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "institutionID","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "computedStateFips","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "license","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "geodeticDatum","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "stateProvince","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "coordinatePrecision","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "year","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "resourceID","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "providedCounty","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "providedState","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "institutionCode","TEXT" "", "",500 )
	arcpy.AddField_management(fc, "bisonID","TEXT" "", "",500 )
	
except Exception as e:
	print e.message

#Create a cursor for the featureclass and fields
cursor = arcpy.da.InsertCursor(fc,flds)
#C:\Users\twburton\Desktop\AlaskaBISON\reproject.shp
arcpy.Project_management(clipfeatures, outproject, sr)#reproject polygon to bison format
clipfeatures=outproject
#inserting data into cursor
for i in range(len(a)):
	
	
	pnt=float(b[i]),float(c[i])#Point data
	row2=(pnt,a[i],d[i],e[i],z[i],f[i],g[i],h[i],j[i],k[i],l[i],m[i],n[i],o[i],p[i],q[i],r[i],s[i],t[i],u[i],v[i],w[i],x[i],y[i]) #data 
	cursor.insertRow(row2)
	
del cursor
arcpy.AddMessage("3--------")
clipfeature2 = outclipfeature + "\\"+featureclassname
#clip data to parks shapefile
infeatures = os.path.join(gdb,fcname)  
arcpy.MakeFeatureLayer_management(infeatures, 'pointslyr')
arcpy.SelectLayerByLocation_management ('pointslyr', "intersect", clipfeatures) #clip using select by location then save selected features
arcpy.SaveToLayerFile_management ('pointslyr', clipfeature2)
arcpy.CopyFeatures_management(clipfeature2+".lyr",clipfeature2+"clipped")
#arcpy.Clip_analysis(infeatures, clipfeatures, outclipfeature + "\\"+featureclassname)
