# coding: utf-8
import csv, pandas, re, keras

class DataReader(object):

    def __init__(self, filename):
        self.__d = pandas.read_csv(filename, sep="\t")

    def get_data(self):
        tyakujun = []
        data = []
        for i in self.__d.index:
            row = self.__d.ix[i]
            tyakujun.append([row["tyakujun"]])
            match = re.search("([0-9]+)月", row["Day"])
            month = int(match.group(1))
            data.append([
                month,
                row["Tokyo"],
                row["Kyoto"],
                row["Nakayama"],
                row["Hanshin"],
                row["Tyukyo"],
                row["Niigata"],
                row["Fukushima"],
                row["Sapporo"],
                row["Hakodate"],
                row["Raceday"],
                # このあたりのデータは扱いが難しいので一旦省くことにした
                #row["First"],
                #row["Maiden"],
                #row["Under500"],
                #row["Under1000"],
                #row["Under1600"],
                #row["Open"],
                #row["G3"],
                #row["G2"],
                #row["G1"],
                row["Grass"],
                row["Dirt"],
                row["Distance"],
                row["LightCo"],
                row["LittleHeavyCo"],
                row["HeavyCo"],
                row["BadCo"],
                row["wakuban"],
                row["Umaban"],
                row["Male"],
                row["Female"],
                row["Senba"],
                row["barei"],
                row["kinryou"],
                row["RunningTime"],
                row["Weight"],
                row["zougen"],
            ])
        return [data, tyakujun]

class TrainModel(object):

    def train(self, data):
        print "start training"
        traindata = data[0]
        dim = len(traindata[0])
        lavel = data[1]
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(32, activation="relu", input_dim=dim))
        model.add(keras.layers.Dense(32, activation="relu"))
        model.add(keras.layers.Dense(1))


        model.compile("sgd", "mse")
        model.fit(traindata, lavel)
        print "end training"


if __name__ == '__main__':
    reader = DataReader("keibadata1000.tsv")
    data = reader.get_data()
    trainer = TrainModel()
    trainer.train(data)

    reader100 = DataReader("keibadata100.tsv")
    testdata = reader100.get_data()
