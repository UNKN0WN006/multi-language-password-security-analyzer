package com.passwordanalyzer.controller;

import com.passwordanalyzer.model.PasswordRequest;
import com.passwordanalyzer.model.PasswordResponse;
import com.passwordanalyzer.service.PasswordService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/password")
public class PasswordController {

    private final PasswordService passwordService;

    @Autowired
    public PasswordController(PasswordService passwordService) {
        this.passwordService = passwordService;
    }

    @PostMapping("/analyze")
    public ResponseEntity<PasswordResponse> analyzePassword(@RequestBody PasswordRequest request) {
        PasswordResponse response = passwordService.analyzePassword(request);
        return ResponseEntity.ok(response);
    }

    @GetMapping("/hash/{algorithm}")
    public ResponseEntity<String> hashPassword(@RequestParam String password, @PathVariable String algorithm) {
        String hashedPassword = passwordService.hashPassword(password, algorithm);
        return ResponseEntity.ok(hashedPassword);
    }
}