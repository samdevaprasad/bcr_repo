import json
import sys
import operator
import numpy as np
import sklearn.cluster 
import distance
import time
from pprint import pprint
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import Birch

start_time = time.time()
file = 'BCR_strings_length_full_occ100'
data = json.load(open(file + '.json'))
sys.stderr.write(str(time.time()-start_time)+'seconds to load data \n')

start_time2 = time.time()
words = np.asarray(data) #So that indexing with a list will work
print(len(words))
lev_similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2 in words])
sys.stderr.write(str(time.time()-start_time2)+'seconds to load data & lev \n')

start_time3 = time.time()
kmeans3 = KMeans(n_clusters=3)
kmeans3.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time3)+'seconds to cluster 3 \n')

start_time4 = time.time()
kmeans10 = KMeans(n_clusters=10)
kmeans10.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time4)+'seconds to cluster 10 \n')

start_time5 = time.time()
kmeans50 = KMeans(n_clusters=50)
kmeans50.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time5)+'seconds to cluster 50 \n')

start_time6 = time.time()
kmeans100 = KMeans(n_clusters=100)
kmeans100.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time6)+'seconds to cluster 100 \n')

start_time7 = time.time()
kmeans1000 = KMeans(n_clusters=1000)
kmeans1000.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time7)+'seconds to cluster 1000 \n')

to_clust = np.exp(-1*lev_similarity)
start_time8 = time.time()
spectralclustering = SpectralClustering(affinity='precomputed')
spectralclustering.fit(to_clust)
sys.stderr.write(str(time.time()-start_time8)+'seconds to spectral cluster \n')

start_time9 = time.time()
ward_clustering = AgglomerativeClustering()
ward_clustering.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time9)+'seconds to ward cluster \n')

start_time10 = time.time()
birch_clustering = Birch()
birch_clustering.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time10)+'seconds to birch cluster \n')

to_clust = np.exp(-1*lev_similarity)
start_time11 = time.time()
spectralclustering_10 = SpectralClustering(affinity='precomputed', n_clusters=10)
spectralclustering_10.fit(to_clust)
sys.stderr.write(str(time.time()-start_time11)+'seconds to spectral cluster 10 \n')

start_time12 = time.time()
ward_clustering_10 = AgglomerativeClustering(n_clusters=10)
ward_clustering_10.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time12)+'seconds to ward cluster 10 \n')

start_time13 = time.time()
birch_clustering_10 = Birch(n_clusters=10)
birch_clustering_10.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time13)+'seconds to birch cluster 10 \n')

to_clust = np.exp(-1*lev_similarity)
start_time14 = time.time()
spectralclustering_50 = SpectralClustering(affinity='precomputed', n_clusters=50)
spectralclustering_50.fit(to_clust)
sys.stderr.write(str(time.time()-start_time14)+'seconds to spectral cluster 50 \n')

start_time15 = time.time()
ward_clustering_50 = AgglomerativeClustering(n_clusters=50)
ward_clustering_50.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time15)+'seconds to ward cluster 50 \n')

start_time16 = time.time()
birch_clustering_50 = Birch(n_clusters=50)
birch_clustering_50.fit(lev_similarity)
sys.stderr.write(str(time.time()-start_time16)+'seconds to birch cluster 50 \n')

start_time8 = time.time()
orig_stdout = sys.stdout
f = open(file + '_clusters.json', 'w')
sys.stdout = f
print json.dumps({ "spectralclustering" : spectralclustering.labels_.tolist(), 
	             "ward_clustering" : ward_clustering.labels_.tolist(),
                   "birch_clustering" : birch_clustering.labels_.tolist(), 
                   "spectralclustering_10" : spectralclustering_10.labels_.tolist(),
                   "ward_clustering_10" : ward_clustering_10.labels_.tolist(),
                   "birch_clustering_10" : birch_clustering_10.labels_.tolist(),
                   "spectralclustering_50" : spectralclustering_50.labels_.tolist(),
                   "ward_clustering_50" : ward_clustering_50.labels_.tolist(),
                   "birch_clustering_50" : birch_clustering_50.labels_.tolist(),
                   "cluster3" : kmeans3.labels_.tolist(), 
                   "cluster10" : kmeans10.labels_.tolist(),
                   "cluster50" : kmeans50.labels_.tolist(), 
                   "cluster100" : kmeans100.labels_.tolist(), 
                   "clusters1000" : kmeans1000.labels_.tolist() 
                   	   })
# print json.dumps({"cluster50" : kmeans50.labels_.tolist() , "cluster100" : kmeans100.labels_.tolist(), "clusters1000" : kmeans1000.labels_.tolist() })
sys.stdout = orig_stdout
f.close()
sys.stderr.write(str(time.time()-start_time8)+'seconds to json dump \n')

sys.stderr.write(str(time.time()-start_time)+'seconds to complete \n')