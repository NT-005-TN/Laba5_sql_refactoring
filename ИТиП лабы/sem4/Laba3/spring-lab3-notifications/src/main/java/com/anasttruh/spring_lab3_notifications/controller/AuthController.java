package com.anasttruh.spring_lab3_notifications.controller;

import com.anasttruh.spring_lab3_notifications.model.dto.RegisterRequest;
import com.anasttruh.spring_lab3_notifications.service.AuthService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
@RequiredArgsConstructor
public class AuthController {

    private final AuthService authService;

    @PostMapping("/register")
    public String register(@RequestBody @Valid RegisterRequest request) {
        authService.register(request);
        return "Пользователь успешно зарегистрирован";
    }

    @PostMapping("/register-admin")
    public String registerAdmin(@RequestBody @Valid RegisterRequest request) {
        authService.registerAdmin(request);
        return "Администратор успешно зарегистрирован";
    }
}
