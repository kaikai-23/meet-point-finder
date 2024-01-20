# 優先キューを使用
import heapq

# まずは線形路線（東山線）のみで実装してみる
stations = {
	# 名古屋市営地下鉄東山線
	'高畑': {'八田': 2},
	'八田': {'高畑': 2, '岩塚': 1},
	'岩塚': {'八田': 1, '中村公園': 2},
	'中村公園': {'岩塚': 2, '中村日赤': 2},
	'中村日赤': {'中村公園': 2, '本陣': 1},
	'本陣': {'中村日赤': 1, '亀島': 2},
	'亀島': {'本陣': 2, '東山線名古屋': 2},
	'東山線名古屋': {'亀島': 2, '東山線伏見': 3, '桜通線名古屋': 10},
	'東山線伏見': {'東山線名古屋': 3, '東山線栄': 2, '鶴舞線伏見': 10},
	'東山線栄': {'東山線伏見': 2, '新栄町': 2, '名城線栄': 7},
	'新栄町': {'東山線栄': 2, '千種': 2},
	'千種': {'新栄町': 2, '東山線今池': 2},
	'東山線今池': {'千種': 2, '池下': 2, '桜通線今池': 10},
	'池下': {'東山線今池': 2, '覚王山': 1},
	'覚王山': {'池下': 1, '東山線本山': 2},
	'東山線本山': {'覚王山': 2, '東山公園': 2, '名城線本山': 7},
	'東山公園': {'東山線本山': 2, '星ヶ丘': 2},
	'星ヶ丘': {'東山公園': 2, '一社': 2},
	'一社': {'星ヶ丘': 2, '上社': 2},
	'上社': {'一社': 2, '本郷': 2},
	'本郷': {'上社': 2, '藤が丘': 2},
	'藤が丘': {'本郷': 2},

	# 名古屋市営地下鉄名城線
    'ナゴヤドーム前矢田': {'大曽根': 1, '砂田橋': 2},
    '大曽根': {'ナゴヤドーム前矢田': 1, '名城線平安通': 1},
    '名城線平安通': {'大曽根': 1, '志賀本通': 1, '上飯田線平安通': 10},
    '志賀本通': {'名城線平安通': 1, '黒川': 2},
    '黒川': {'志賀本通': 2, '名城公園': 2},
    '名城公園': {'黒川': 2, '名古屋城': 2},
    '名古屋城': {'名城公園': 2, '名城線久屋大通': 2},
    '名城線久屋大通': {'名古屋城': 2, '名城線栄': 1, '桜通線久屋大通': 10},
	'名城線栄': {'名城線久屋大通': 1, '矢場町': 2, '東山線栄': 5},
    '矢場町': {'名城線栄': 1, '名城線上前津': 1},
    '名城線上前津': {'矢場町': 2, '東別院': 2, '鶴舞線上前津': 10},
    '東別院': {'名城線上前津': 2, '名城線金山': 2},
    '名城線金山': {'東別院': 2, '西高蔵': 2, '名港線金山': 10},
    '西高蔵': {'名城線金山': 2, '熱田神宮西': 2},
    '熱田神宮西': {'西高蔵': 2, '熱田神宮伝馬町': 1},
    '熱田神宮伝馬町': {'熱田神宮西': 1, '堀田': 2},
    '堀田': {'熱田神宮伝馬町': 2, '妙音通': 2},
    '妙音通': {'堀田': 2, '名城線新瑞橋': 1},
    '名城線新瑞橋': {'妙音通': 1, '瑞穂運動場東': 2, '桜通線新瑞橋': 10},
    '瑞穂運動場東': {'名城線新瑞橋': 2, '総合リハビリセンター': 2},
    '総合リハビリセンター': {'瑞穂運動場東': 2, '名城線八事': 2},
    '名城線八事': {'総合リハビリセンター': 2, '八事日赤': 2, '鶴舞線八事': 10},
    '八事日赤': {'名城線八事': 2, '名古屋大学': 2},
    '名古屋大学': {'八事日赤': 2, '名城線本山': 1},
	'名城線本山':{'名古屋大学': 1, '自由ヶ丘': 2, '東山線本山': 5},
    '自由ヶ丘': {'名城線本山': 1, '茶屋ヶ坂': 2},
    '茶屋ヶ坂': {'自由ヶ丘': 2, '砂田橋': 2},
    '砂田橋': {'茶屋ヶ坂': 2, 'ナゴヤドーム前矢田': 2},

	# 名古屋市営地下鉄名港線
    '名港線金山':{'名城線金山': 10, '日比野': 2},
	'日比野': {'名港線金山': 2, '六番町': 2},
    '六番町': {'日比野': 2, '東海通': 2},
    '東海通': {'六番町': 2, '港区役所': 1},
    '港区役所': {'東海通': 1, '築地口': 2},
    '築地口': {'港区役所': 2, '名古屋港': 1},
    '名古屋港': {'築地口': 1},

	# 名古屋市営地下鉄鶴舞線
	'上小田井':{'庄内緑地公園': 2},
	'庄内緑地公園':{'上小田井': 2, '庄内通': 2},
	'庄内通':{'庄内緑地公園': 2, '浄心': 2},
	'浄心':{'庄内通': 2, '浅間町': 1},
	'浅間町':{'浄心': 1, '鶴舞線丸の内': 2},
	'鶴舞線丸の内':{'浅間町': 2, '鶴舞線伏見': 2, '桜通線丸の内': 13},
	'鶴舞線伏見':{'鶴舞線丸の内': 2, '大須観音': 1, '東山線伏見': 7},
	'大須観音':{'鶴舞線伏見': 1, '鶴舞線上前津': 3},
	'鶴舞線上前津':{'大須観音': 3, '鶴舞': 1, '名城線上前津': 10},
	'鶴舞':{'鶴舞線上前津': 1, '荒畑': 2},
	'荒畑':{'鶴舞': 2, '鶴舞線御器所': 2},
	'鶴舞線御器所':{'荒畑': 2, '川名': 2, '桜通線御器所': 10},
	'川名':{'鶴舞線御器所': 2, 'いりなか': 2},
	'いりなか':{'川名': 2, '鶴舞線八事': 2},
	'鶴舞線八事':{'いりなか': 2, '塩釜口': 2, '名城線八事': 10},
	'塩釜口':{'鶴舞線八事': 2, '植田': 2},
	'植田':{'塩釜口': 2, '原': 2},
	'原':{'植田': 2, '平針': 1},
	'平針':{'原': 1, '赤池': 2},
	'赤池':{'平針': 2},

	# 名古屋市営地下鉄桜通線
	'太閤通':{'桜通線名古屋': 2},
	'桜通線名古屋':{'太閤通': 2, '国際センター': 2, '東山線名古屋': 7},
	'国際センター':{'桜通線名古屋': 2, '桜通線丸の内': 1},
	'桜通線丸の内':{'国際センター': 1, '桜通線久屋大通': 2, '鶴舞線丸の内': 10},
	'桜通線久屋大通':{'桜通線丸の内': 2, '高岳': 2, '名城線久屋大通': 10},
	'高岳':{'桜通線久屋大通': 2, '車道': 2},
	'車道':{'高岳': 2, '桜通線今池': 2},
	'桜通線今池':{'車道': 2, '吹上': 2, '東山線今池': 7},
	'吹上':{'桜通線今池': 2, '桜通線御器所': 2},
	'桜通線御器所':{'吹上': 2, '桜山': 2, '鶴舞線御器所': 10},
	'桜山':{'桜通線御器所': 2, '瑞穂区役所': 2},
	'瑞穂区役所':{'桜山': 2, '瑞穂運動場西': 1},
	'瑞穂運動場西':{'瑞穂区役所': 1, '桜通線新瑞橋': 2},
	'桜通線新瑞橋':{'瑞穂運動場西': 2, '桜本町': 2, '名城線新瑞橋': 10},
	'桜本町':{'桜通線新瑞橋': 2, '鶴里': 2},
	'鶴里':{'桜本町': 2, '野並': 2},
	'野並':{'鶴里': 2, '鳴子北': 2},
	'鳴子北':{'野並': 2, '相生山': 2},
	'相生山':{'鳴子北': 2, '神沢': 2},
	'神沢':{'相生山': 2, '徳重': 1},
	'徳重':{'神沢': 1},

	# 名古屋市営地下鉄上飯田線
	'上飯田線平安通':{'上飯田駅': 2, '名城線平安通': 10},
	'上飯田駅':{'上飯田線平安通': 2}
}

# ダイクストラ法を用いてそれぞれの駅に対する最短距離を求める関数
def find_minimum_time(start_station, stations):
	# 優先キューの初期化:(所要時間, 駅名)のタプルで管理
	queue = [(0, start_station)]

	# 各駅までの最短所要時間初期化:無限大（inf）に設定
	distances = {station: float('inf') for station in stations}
	# 開始駅の所要時間は0に設定
	distances[start_station] = 0

	while queue:
		# 現時点で最短所要時間の駅を取り出す
		current_distance, current_station = heapq.heappop(queue)

		# 既に最短時間が見つかっている場合はスキップ
		if current_distance > distances[current_station]:
			continue
		
		# 隣接駅の所要時間を確認し、必要に応じて更新
		for neighbor, weight in stations[current_station].items():
			# 開始駅から隣接駅までの総所要時間
			distance = current_distance + weight
			# 隣接駅の最短所要時間を更新し、キューに追加
			if distance < distances[neighbor]:
				distances[neighbor] = distance
				heapq.heappush(queue, (distance, neighbor))
	return distances


if __name__=="__main__":
	# 始発駅入力
	start_stations = ["上小田井", "いりなか", "本郷"]
	# start_stations = ["上小田井", "いりなか"]
	print("<始発駅一覧>")
	for start_station in start_stations:
		print(f"・{start_station}駅")
	print("\n- - - - - - - - - - - - - - - -\n")

	# 始発駅の内、最も遠い駅から各駅までの所要時間を保存
	minimum_time_from_farthest_station = {}
	# 最も遠い駅からの所要時間を0で初期化: {'駅名': 所要時間}
	for station in stations.keys():
		minimum_time_from_farthest_station[station] = 0

	# print(minimum_time_from_farthest_station)

	# 各始発駅から全駅への最短所要時間を計算し、最も遠い駅からの所要時間を更新
	for start_station in start_stations:
		time_from_start_station = find_minimum_time(start_station, stations)
		for name in time_from_start_station.keys():
			# 最も遠い駅が見つかった場合、最も遠い駅からの所要時間を更新
			if minimum_time_from_farthest_station[name] < time_from_start_station[name]:
				minimum_time_from_farthest_station[name] = time_from_start_station[name]
	
	# 早い順にソート
	sorted_minimum_time = sorted(minimum_time_from_farthest_station.items(), key=lambda x: x[1])
	# print(sorted_minimum_time)

	print("<候補駅一覧>")
	print()
	i = 0
	for candidate_station, minutes in sorted_minimum_time:
		if i == 5:
			break
		print(f"候補駅{i+1}: 「{candidate_station}」")
		# print(f"<所要時間>")
		for start_station in start_stations:
			time_from_start_station = find_minimum_time(start_station, stations)[candidate_station]
			print(f"{start_station}から{time_from_start_station}分")
		print()
		i += 1