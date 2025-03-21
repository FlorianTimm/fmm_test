# basierend auf dem Beispiel https://github.com/cyang-kth/fmm/blob/master/example/notebook/fmm_example.ipynb

# import pandas as pd
from fmm import Network, NetworkGraph, FastMapMatch, FastMapMatchConfig, \
    UBODT, UBODTGenAlgorithm

network = Network("./netz.shp")
print("Nodes {} edges {}".format(
    network.get_node_count(), network.get_edge_count()))
graph = NetworkGraph(network)

ubodt_gen = UBODTGenAlgorithm(network, graph)

status = ubodt_gen.generate_ubodt("./ubodt.txt", 4, binary=False, use_omp=True)
print(status)

ubodt = UBODT.read_ubodt_csv("./ubodt.txt")

model = FastMapMatch(network, graph, ubodt)

k = 8
radius = 100
gps_error = 50
fmm_config = FastMapMatchConfig(k, radius, gps_error)
wkt = "LineString (576949.15 5945348.15, 576933.11 5945300.79, 576917.07 5945253.43, 576901.04 5945206.08, 576882.21 5945160.07, 576855.10 5945118.05, 576828.00 5945076.03, 576800.91 5945034.01, 576773.81 5944991.99, 576746.71 5944949.97, 576719.61 5944907.95, 576698.74 5944862.78, 576680.92 5944816.06, 576643.57 5944785.68, 576600.73 5944759.89, 576556.99 5944736.50, 576507.82 5944727.42, 576458.65 5944718.34, 576409.48 5944709.27, 576360.31 5944700.19, 576311.14 5944691.11, 576261.84 5944683.04, 576211.99 5944679.25, 576162.13 5944675.46, 576112.27 5944671.67, 576064.34 5944660.34, 576018.77 5944639.76, 575997.93 5944598.26, 575985.17 5944549.92, 575977.27 5944500.89, 575976.26 5944450.90, 575975.24 5944400.91, 575974.23 5944350.92, 575972.43 5944300.97, 575968.53 5944251.12, 575964.63 5944201.28, 575947.70 5944156.89, 575914.88 5944119.17, 575882.06 5944081.45, 575849.47 5944043.53, 575817.92 5944004.75, 575786.37 5943965.96, 575754.81 5943927.18, 575712.41 5943900.76, 575667.18 5943883.01, 575617.26 5943880.20, 575567.34 5943877.39, 575542.71 5943836.48, 575502.82 5943816.34, 575452.83 5943817.28, 575402.84 5943818.21, 575352.85 5943819.14, 575302.86 5943820.07, 575304.75 5943778.93, 575315.99 5943730.21, 575327.23 5943681.49, 575319.31 5943643.19, 575272.30 5943626.15, 575225.29 5943609.11, 575178.28 5943592.08, 575131.28 5943575.04, 575112.30 5943538.06, 575097.42 5943498.13, 575050.46 5943480.95, 575003.51 5943463.77, 574956.55 5943446.58, 574923.47 5943419.49, 574922.45 5943369.50, 574921.42 5943319.51, 574920.40 5943269.52, 574919.38 5943219.54, 574918.35 5943169.55, 574917.45 5943119.55, 574916.77 5943069.56, 574916.08 5943019.56, 574915.40 5942969.57, 574914.71 5942919.57, 574867.32 5942906.87, 574818.72 5942895.14, 574770.11 5942883.41, 574721.51 5942871.67, 574672.90 5942859.94, 574624.30 5942848.20, 574575.70 5942836.47, 574570.49 5942791.00, 574571.11 5942741.00, 574571.54 5942691.15, 574522.97 5942679.27, 574474.40 5942667.39, 574425.83 5942655.51, 574377.26 5942643.63, 574328.69 5942631.76, 574282.63 5942612.66, 574237.16 5942591.86, 574230.44 5942542.67, 574224.30 5942493.05, 574218.16 5942443.43, 574212.03 5942393.81, 574205.89 5942344.18, 574199.75 5942294.56, 574193.62 5942244.94, 574187.48 5942195.32, 574181.35 5942145.70, 574175.21 5942096.07, 574136.30 5942067.57, 574093.65 5942041.46, 574051.01 5942015.35, 574013.22 5941987.39, 574028.62 5941939.82, 574044.02 5941892.24, 574058.31 5941844.39, 574067.69 5941795.28, 574077.07 5941746.17, 574086.45 5941697.05, 574095.83 5941647.94, 574105.21 5941598.83, 574122.28 5941552.77, 574149.13 5941510.59, 574175.98 5941468.41, 574202.83 5941426.23, 574239.80 5941399.40, 574289.15 5941391.36, 574322.75 5941360.40, 574319.24 5941310.52, 574315.73 5941260.64, 574322.30 5941211.35, 574331.57 5941162.22, 574347.01 5941114.82, 574360.20 5941067.09, 574362.97 5941017.16, 574362.96 5940967.67, 574345.12 5940920.96, 574327.27 5940874.26, 574308.52 5940827.91, 574289.05 5940781.86, 574269.57 5940735.81, 574250.09 5940689.76, 574230.61 5940643.71, 574211.14 5940597.66, 574191.66 5940551.61, 574172.18 5940505.56, 574152.70 5940459.51, 574133.23 5940413.46, 574113.75 5940367.41, 574094.27 5940321.36, 574074.79 5940275.31, 574055.31 5940229.26, 574027.40 5940187.97, 573998.07 5940147.47, 573968.74 5940106.98, 573939.42 5940066.48, 573910.09 5940025.99, 573880.76 5939985.49, 573852.20 5939944.51, 573827.87 5939900.83, 573803.54 5939857.15, 573779.21 5939813.47, 573754.87 5939769.79, 573735.77 5939724.00, 573722.99 5939675.66, 573710.21 5939627.32, 573692.81 5939580.77, 573657.90 5939550.47, 573609.41 5939538.44, 573560.56 5939527.77, 573511.71 5939517.09, 573462.87 5939506.42, 573414.02 5939495.74, 573365.17 5939485.06, 573316.33 5939474.39, 573267.48 5939463.71, 573220.50 5939447.79, 573175.93 5939425.14, 573131.35 5939402.50, 573086.77 5939379.86, 573042.19 5939357.22, 572997.10 5939335.70, 572950.58 5939317.38, 572904.05 5939299.07, 572857.53 5939280.75, 572811.00 5939262.43, 572764.48 5939244.12, 572717.96 5939225.80, 572671.43 5939207.48, 572669.10 5939160.46, 572671.27 5939110.51, 572673.45 5939060.56, 572675.63 5939010.61, 572677.81 5938960.65, 572678.98 5938910.82, 572664.86 5938862.86, 572634.36 5938830.31, 572587.34 5938813.30, 572540.32 5938796.30, 572493.30 5938779.29, 572446.28 5938762.29, 572399.26 5938745.29, 572352.24 5938728.28, 572305.22 5938711.28, 572258.20 5938694.27, 572211.18 5938677.27, 572164.16 5938660.27, 572117.14 5938643.26, 572070.12 5938626.26, 572023.10 5938609.25, 571976.08 5938592.25, 571929.06 5938575.25, 571882.04 5938558.24, 571835.02 5938541.24, 571788.00 5938524.23, 571740.98 5938507.23, 571693.96 5938490.23, 571646.94 5938473.22, 571599.92 5938456.22, 571552.90 5938439.21, 571505.89 5938422.21, 571458.87 5938405.21, 571411.85 5938388.20, 571364.71 5938371.67, 571315.26 5938364.28, 571265.81 5938356.89, 571216.35 5938349.50, 571177.16 5938330.32, 571163.02 5938282.36, 571148.88 5938234.41, 571134.74 5938186.45, 571120.60 5938138.49, 571106.45 5938090.53, 571089.08 5938043.66, 571071.21 5937996.97, 571053.33 5937950.28, 571035.45 5937903.58, 571017.57 5937856.89, 570999.69 5937810.19, 570981.81 5937763.50, 570963.93 5937716.80, 570936.83 5937674.93, 570908.72 5937633.58, 570880.61 5937592.23, 570852.50 5937550.88, 570824.38 5937509.53, 570796.27 5937468.18, 570767.73 5937427.32, 570723.14 5937404.70, 570678.55 5937382.09, 570633.96 5937359.47, 570594.97 5937329.89, 570563.37 5937291.14, 570531.77 5937252.39, 570505.75 5937231.61, 570514.01 5937191.59, 570474.08 5937161.49, 570434.16 5937131.39, 570394.24 5937101.29, 570355.74 5937069.45, 570318.41 5937036.19, 570281.07 5937002.92, 570243.74 5936969.66, 570205.94 5936937.12, 570160.55 5936916.15, 570115.16 5936895.18, 570069.43 5936875.00, 570022.85 5936856.83, 569976.27 5936838.65, 569930.37 5936818.89, 569884.98 5936797.92, 569839.59 5936776.95, 569796.97 5936751.03, 569755.43 5936723.21, 569713.89 5936695.38, 569673.39 5936666.07, 569628.24 5936646.14, 569580.45 5936631.43, 569533.39 5936614.68, 569487.17 5936595.62, 569440.95 5936576.56, 569394.54 5936557.95, 569347.96 5936539.78, 569301.13 5936522.89, 569251.13 5936522.50, 569201.13 5936522.11, 569161.23 5936496.58, 569138.48 5936452.98, 569097.92 5936427.42, 569052.53 5936406.46, 569007.13 5936385.50, 568961.74 5936364.54, 568916.34 5936343.58, 568870.95 5936322.62, 568829.44 5936295.74, 568792.09 5936262.49, 568754.75 5936229.24, 568717.41 5936195.99, 568680.06 5936162.74, 568642.72 5936129.49, 568605.38 5936096.25, 568568.04 5936062.99, 568530.94 5936029.47, 568493.85 5935995.94, 568456.76 5935962.41, 568419.66 5935928.89, 568382.57 5935895.36, 568345.47 5935861.83, 568308.38 5935828.31, 568261.69 5935832.90, 568213.14 5935844.86, 568164.59 5935856.82, 568115.90 5935857.27, 568067.07 5935846.51, 568019.09 5935834.03, 567980.56 5935802.15, 567944.17 5935767.96, 567909.17 5935732.25, 567863.61 5935720.26, 567813.65 5935718.13, 567763.70 5935716.00, 567713.74 5935713.87, 567663.79 5935711.73, 567613.84 5935709.60, 567565.62 5935703.83, 567532.67 5935666.23, 567499.72 5935628.62, 567466.77 5935591.02, 567433.81 5935553.41, 567401.01 5935515.68, 567368.87 5935477.37, 567336.74 5935439.07, 567304.60 5935400.77, 567272.46 5935362.46, 567240.32 5935324.16, 567208.19 5935285.86, 567176.05 5935247.55, 567143.91 5935209.25, 567109.82 5935172.71, 567074.82 5935137.01, 567039.12 5935102.10, 566999.17 5935072.03, 566959.23 5935041.95, 566917.46 5935014.76, 566873.18 5934991.54, 566828.90 5934968.33, 566787.36 5934940.77, 566747.41 5934910.70, 566707.46 5934880.63, 566667.52 5934850.56, 566627.57 5934820.49, 566587.62 5934790.42, 566547.67 5934760.35, 566507.73 5934730.28, 566467.78 5934700.21, 566427.83 5934670.14, 566388.93 5934638.83, 566352.53 5934604.56, 566316.12 5934570.28, 566280.97 5934534.80, 566248.01 5934497.20, 566215.05 5934459.60, 566182.08 5934422.01, 566148.68 5934384.83, 566112.77 5934350.04, 566076.87 5934315.24, 566040.97 5934280.44, 566005.06 5934245.64, 565969.16 5934210.84, 565933.25 5934176.05, 565894.58 5934144.42)"

result = model.match_wkt(wkt, fmm_config)

print("Matched path: ", list(result.cpath))
print("Matched edge for each point: ", list(result.opath))
print("Matched edge index ", list(result.indices))
print("Matched geometry: ", result.mgeom.export_wkt())
print("Matched point ", result.pgeom.export_wkt())

candidates = []
txt = open("candidates.csv", "w")
txt.write("eid,source,target,error,length,offset,spdist,ep,tp\n")
txt.close()
for c in result.candidates:
    txt = open("candidates.csv", "a")
    txt.write("{},{},{},{},{},{},{},{},{}\n".format(c.edge_id, c.source, c.target, c.error,
                                                    c.length, c.offset, c.spdist, c.ep, c.tp))
    txt.close()
    candidates.append((c.edge_id, c.source, c.target, c.error,
                      c.length, c.offset, c.spdist, c.ep, c.tp))

# df = pd.DataFrame(candidates,
#                   columns=["eid", "source", "target", "error", "length",
#                            "offset", "spdist", "ep", "tp"])
# df.head()
