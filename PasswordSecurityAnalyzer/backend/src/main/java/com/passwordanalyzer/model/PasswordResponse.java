package com.passwordanalyzer.model;

public class PasswordResponse {
    private String password;
    private boolean isSecure;
    private String strength;
    private String[] recommendations;

    public PasswordResponse(String password, boolean isSecure, String strength, String[] recommendations) {
        this.password = password;
        this.isSecure = isSecure;
        this.strength = strength;
        this.recommendations = recommendations;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public boolean isSecure() {
        return isSecure;
    }

    public void setSecure(boolean secure) {
        isSecure = secure;
    }

    public String getStrength() {
        return strength;
    }

    public void setStrength(String strength) {
        this.strength = strength;
    }

    public String[] getRecommendations() {
        return recommendations;
    }

    public void setRecommendations(String[] recommendations) {
        this.recommendations = recommendations;
    }
}