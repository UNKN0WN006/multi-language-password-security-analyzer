package com.passwordanalyzer.model;

public class HashComparison {
    private String algorithm;
    private String hashValue;

    public HashComparison(String algorithm, String hashValue) {
        this.algorithm = algorithm;
        this.hashValue = hashValue;
    }

    public String getAlgorithm() {
        return algorithm;
    }

    public void setAlgorithm(String algorithm) {
        this.algorithm = algorithm;
    }

    public String getHashValue() {
        return hashValue;
    }

    public void setHashValue(String hashValue) {
        this.hashValue = hashValue;
    }

    @Override
    public String toString() {
        return "HashComparison{" +
                "algorithm='" + algorithm + '\'' +
                ", hashValue='" + hashValue + '\'' +
                '}';
    }
}