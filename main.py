import functions



def main():
    d = [1, 2, 3, 4, 5, 5, 10, 100]

    mean = functions.CalculateMean()
    standard_deviation = functions.CalculateStandardDeviation()
    

    for i in d:
        mean_value = mean.add_data(i)
        standard_deviation_value = standard_deviation.add_data(i)

        print("MEAN:", mean_value)
        print("STDEV: ", standard_deviation_value)
        pdf = functions.CalculateGaussianDistribution(mean_value, standard_deviation_value)
        print(pdf.mean)
        print(pdf.std_dev)
        print("PDF: ", pdf.calculate_pdf(1))

        print(i)




if __name__ == "__main__":
    main()