package com.passwordanalyzer.service;

import com.passwordanalyzer.model.PasswordRequest;
import com.passwordanalyzer.model.PasswordResponse;
import org.springframework.stereotype.Service;

@Service
public class PasswordService {

    public PasswordResponse analyzePassword(PasswordRequest request) {
        PasswordResponse response = new PasswordResponse();
        
        // Implement password strength analysis logic here
        // For example, check length, character variety, etc.
        int strengthScore = calculateStrengthScore(request.getPassword());
        response.setStrengthScore(strengthScore);
        
        // Add additional analysis results to the response
        response.setSuggestions(generateSuggestions(request.getPassword(), strengthScore));
        
        return response;
    }

    private int calculateStrengthScore(String password) {
        // Placeholder for actual strength calculation logic
        int score = 0;
        if (password.length() >= 12) score++;
        if (password.matches(".*[A-Z].*")) score++;
        if (password.matches(".*[a-z].*")) score++;
        if (password.matches(".*[0-9].*")) score++;
        if (password.matches(".*[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>\\/?].*")) score++;
        return score;
    }

    private String[] generateSuggestions(String password, int strengthScore) {
        // Placeholder for generating improvement suggestions
        return new String[] {
            "Consider adding more characters.",
            "Use a mix of uppercase and lowercase letters.",
            "Include numbers and special characters."
        };
    }
}