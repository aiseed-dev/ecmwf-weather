## ecmwf-weather

ヨーロッパ中期予報センターがオープンデータとして提供するリアルタイム予報データ及び再解析データERA5の利用について

## リアルタイム予報データ

### 著作権

ECMWF リアルタイム予報データのサブセットは、クリエイティブ コモンズ CC-4.0-BY ライセンスおよび ECMWF 利用規約により無料で一般に公開されています。
このため、適切な帰属を条件として、データを再配布したり商業的に使用したりできます 。

Under the following terms:

    You must give appropriate credit (attribution) to ECMWF as outlined below, provide a link to the licence, and indicate if changes were made.
    No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the licence permits.

The following wording shall be attached to the use of this ECMWF data product: 

    Copyright statement: Copyright "© [year] European Centre for Medium-Range Weather Forecasts (ECMWF)".
    Source www.ecmwf.int
    Licence Statement: This data is published under a Creative Commons Attribution 4.0 International (CC BY 4.0). https://creativecommons.org/licenses/by/4.0/
    Disclaimer: ECMWF does not accept any liability whatsoever for any error or omission in the data, their availability, or for any loss or damage arising from their use.
    Where applicable, an indication if the material has been modified and an indication of previous modifications.

The following wording shall be attached to the services created with this ECMWF data product:

    Copyright statement: Copyright "This service is based on data and products of the European Centre for Medium-Range Weather Forecasts (ECMWF)".
    Source www.ecmwf.int
    Licence Statement: This ECMWF data is published under a Creative Commons Attribution 4.0 International (CC BY 4.0). https://creativecommons.org/licenses/by/4.0/
    Disclaimer: ECMWF does not accept any liability whatsoever for any error or omission in the data, their availability, or for any loss or damage arising from their use.
    Where applicable, an indication if the material has been modified and an indication of previous modifications

You need to log in first in order to accept this licence and terms of use. 

### データへのアクセス
ドキュメント  
[ECMWF open data: real-time forecasts from IFS and AIFS](https://confluence.ecmwf.int/display/DAC/ECMWF+open+data%3A+real-time+forecasts+from+IFS+and+AIFS)

以下のサイトから取得可能

ECMWF: https://data.ecmwf.int/forecasts
Microsoft Azure: https://ai4edataeuwest.blob.core.windows.net/ecmwf
Amazon AWS https://ecmwf-forecasts.s3.eu-central-1.amazonaws.com

### ファイル形式

[ROOT]/[yyyymmdd]/[HH]z/[model]/0p25/[stream]/[yyyymmdd][HH]0000-[step]h-[stream]-[type].grib2
[ROOT]  is the top-level URL of one of the sites hosting the data. See the above for possible values.  
[yyyymmdd] is the reference date of the forecasts (base date).  
[HH] is the reference time of the forecasts. Values are 00, 06 , 12  and 18.    
[model] is the production model (IFS or AIFS).  Note: IFS and AIFS have different options, so please be review dataset pages to see what is available.  
[resol]  is the horizontal resolution of the data. Options include: 0p25 or 0p4-beta  
[stream] is the forecasting system that produces the data.  Values are:  
  - oper - high-resolution forecast, atmospheric fields   
  - enfo - ensemble forecast, atmospheric fields (not applicable for AIFS model)  
  - waef - ensemble forecast, ocean wave fields, (not applicable for AIFS model)  
  - wave - wave model, (not applicable for AIFS model)  
  - scda  - short cut-off high-resolution forecast, atmospheric fields (also known as "high-frequency products") (not applicable for AIFS model)
  - scwv  - short cut-off high-resolution forecast, ocean wave fields (also known as "high-frequency products") (not applicable for AIFS model) and 
  - mmsf  - multi-model seasonal forecasts fields from the ECMWF model only (not applicable for AIFS model).  
  高精度予報、00h, 12h は、oper、06h, 18h は、追加情報で scda。   

[step] is the forecast time step expressed in units U  
　　高精度予報、00h, 12h は、step=0h to 144h by 3h, 144h to 240h by 6h  
　　　　　　　　06h, 18h は、step=0h to 90h by 3h  
[type] is once of fc (forecast), ef (ensemble forecast), ep (ensemble probabilities) or tf (trajectory forecast for tropical cyclone tracks).   
[format] is grib2 for all fields, and bufr for the trajectories.   

### 公開時間
[Dissemination schedule](https://confluence.ecmwf.int/display/DAC/Dissemination+schedule)
有料版の１時間後  
00h 7:55  
06h 13:12  
12h 19:55  
18h 1:12  

### データ項目

[Open data](https://www.ecmwf.int/en/forecasts/datasets/open-data)

|　short name	|	long name	|	日本語	|	ID	|	Level	|
----|----|----|----|----
|	10u	|	10 metre U wind component	|	10メートル風のU成分	|	165	|	Single	|
|	10v	|	10 metre V wind component	|	10メートルV風成分	|	166	|	Single	|
|	100u	|	100 metre U wind component	|	100メートルU風成分	|	228246	|	Single	|
|	100v	|	100 metre V wind component	|	100メートルV風成分	|	228247	|	Single	|
|	2t	|	2 metre temperature	|	2メートル気温	|	167	|	Single	|
|	2d	|	2 metre dewpoint temperature	|	2メートル露点温度	|	168	|	Single	|
|	msl	|	Mean sea level pressure	|	平均海面気圧	|	151	|	Single	|
|	mp2	|	Mean zero-crossing wave period	|	平均ゼロクロッシング波周期	|	140221	|	Single	|
|	mwd	|	Mean wave direction	|	平均波向き	|	140230	|	Single	|
|	mwp	|	Mean wave period	|	平均波周期	|	140232	|	Single	|
|	pp1d	|	Peak wave period	|	ピーク波周期	|	140231	|	Single	|
|	swh	|	Significant height of combined wind waves and swell	|	風波とうねりの合成波の有義高さ	|	140229	|	Single	|
|	ro	|	Runoff	|	流出量	|	205	|	Single	|
|	tp	|	Total Precipitation	|	降水量合計	|	228	|	Single	|
|	sp	|	Surface pressure	|	地表気圧	|	134	|	Single	|
|	st	|	Soil temperature	|	土壌温度	|	228139	|	Single	|
|	tcwv	|	Total column vertically-integrated water vapour	|	総柱状水蒸気	|	137	|	Single	|
|	lsm	|	Land Sea Mask	|	陸海マスク	|	172	|	Single	|
|	swvl1	|	Volumetric soil water layer 1	|	第1土壌水分層の体積水分	|	39	|	Single	|
|	swvl2	|	Volumetric soil water layer 2	|	第2土壌水分層の体積水分	|	40	|	Single	|
|	swvl3	|	Volumetric soil water layer 3	|	第3土壌水分層の体積水分	|	41	|	Single	|
|	swvl4	|	Volumetric soil water layer 4	|	第4土壌水分層の体積水分	|	42	|	Single	|
|	stl1	|	Soil temperature level 1	|	第1土壌温度層	|	139	|	Single	|
|	stl2	|	Soil temperature level 2	|	第2土壌温度層	|	170	|	Single	|
|	stl3	|	Soil temperature level 3	|	第3土壌温度層	|	183	|	Single	|
|	stl4	|	Soil temperature level 4	|	第4土壌温度層	|	236	|	Single	|
|	cape	|	Convective available potential energy	|	対流利用可能ポテンシャルエネルギー	|	59	|	Single	|
|	asn	|	Snow albedo	|	雪のアルベド	|	32	|	Single	|
|	mn2t3	|	Minimum temperature at 2 metres in the last 3 hours - currently unavailable (11/03/2024)	|	過去3時間の2メートル最低気温 - 現在利用不可 (11/03/2024)	|	228027	|	Single	|
|	mx2t3	|	Maximum temperature at 2 metres in the last 3 hours - currently unavailable (11/03/2024)	|	過去3時間の2メートル最高気温 - 現在利用不可 (11/03/2024)	|	228026	|	Single	|
|	ttr	|	Top net long-wave (thermal) radiation	|	大気上端の正味長波（熱）放射	|	179	|	Single	|
|	str	|	Surface net long-wave (thermal) radiation	|	地表の正味長波（熱）放射	|	177	|	Single	|
|	ssr	|	Surface net short-wave (solar) radiation	|	地表の正味短波（太陽）放射	|	176	|	Single	|
|	ssrd	|	Surface net short-wave (solar) radiation downwards	|	地表に向かう正味短波（太陽）放射	|	169	|	Single	|
|	strd	|	Surface net long-wave (thermal) radiation downwards	|	地表に向かう正味長波（熱）放射	|	175	|	Single	|
|	nsss	|	Time-integrated northward turbulent surface stress - currently unavailable (11/03/2024)	|	時間積分された北向きの乱流地表応力 - 現在利用不可 (11/03/2024)	|		|	Single	|
|	ewss	|	Time-integrated eastward turbulent surface stress - currently unavailable (11/03/2024)	|	時間積分された東向きの乱流地表応力 - 現在利用不可 (11/03/2024)	|		|	Single	|
|	t20d	|	Depth of 20C isotherm - currently unavailable (11/03/2024)	|	20℃等温線の深さ - 現在利用不可 (11/03/2024)	|		|	Single	|
|	sav300	|	Average salinity in the upper 300m - currently unavailable (11/03/2024)	|	上位300mの平均塩分 - 現在利用不可 (11/03/2024)	|		|	Single	|
|	ocu	|	Eastward sea water velocity - currently unavailable (11/03/2024)	|	東向きの海水流速 - 現在利用不可 (11/03/2024)	|		|	Single	|
|	ocv	|	Northward sea water velocity - currently unavailable (11/03/2024)	|	北向きの海水流速 - 現在利用不可 (11/03/2024)	|		|	Single	|
|	sithick	|	Sea ice thickness - currently unavailable (11/03/2024)	|	海氷の厚さ - 現在利用不可 (11/03/2024)	|		|	Single	|
|	zos	|	Sea surface height - currently unavailable (11/03/2024)	|	海面高さ - 現在利用不可 (11/03/2024)	|		|	Single	|
|	d	|	Divergence	|	発散	|	155	|	Pressure	|
|	gh	|	Geopotential height	|	地球温暖化の高さ	|	156	|	Pressure	|
|	q	|	Specific humidity	|	特定湿度	|	133	|	Pressure	|
|	r	|	Relative humidity	|	相対湿度	|	157	|	Pressure	|
|	t	|	Temperature	|	気温	|	130	|	Pressure	|
|	u	|	U component of wind	|	風のU成分	|	131	|	Pressure	|
|	v	|	V component of wind	|	風のV成分	|	132	|	Pressure	|
|	w	|	Vertical velocity	|		|	135	|	Pressure	|
|	vo	|	Vorticity (relative)	|		|	138	|	Pressure	|


サブセットだと言っても、00h,12hのデータは全部だと約8GBあります。



