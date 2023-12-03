import functions



def main():
    d = [1, 2, 3, 4, 5, 5, 10, 100]

    mean = functions.CalculateMean()
    standard_deviation = functions.CalculateStandardDeviation()
    

    for i in d:
        mean = mean.add_data(i)
        standard_deviation = standard_deviation.add_data(i)

        print("MEAN:", mean)
        print("STDEV: ", standard_deviation)
        pdf = functions.CalculateGaussianDistribution(mean, standard_deviation)
        pdf.calculate_pdf(0)
        print(i)




if __name__ == "__main__":
    main()