package com.anasttruh.spring_lab3_notifications.service;

import com.anasttruh.spring_lab3_notifications.model.dto.RegisterRequest;
import com.anasttruh.spring_lab3_notifications.model.entity.User;
import com.anasttruh.spring_lab3_notifications.model.enums.UserRole;
import com.anasttruh.spring_lab3_notifications.repository.UserRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class AuthServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @InjectMocks
    private AuthService authService;

    @Test
    void shouldRegisterNewUser() {
        RegisterRequest request = new RegisterRequest();
        request.setName("Анна");
        request.setEmail("anna@example.com");
        request.setPassword("password123");

        when(userRepository.findByEmail(request.getEmail())).thenReturn(Optional.empty());
        when(passwordEncoder.encode(request.getPassword())).thenReturn("encoded_password");

        authService.register(request);

        verify(userRepository, times(1)).findByEmail(request.getEmail());
        verify(passwordEncoder, times(1)).encode(request.getPassword());
        verify(userRepository, times(1)).save(any(User.class));
    }

    @Test
    void shouldThrowExceptionWhenEmailExists() {
        RegisterRequest request = new RegisterRequest();
        request.setEmail("existing@example.com");

        when(userRepository.findByEmail(request.getEmail())).thenReturn(Optional.of(new User()));

        assertThrows(RuntimeException.class, () -> authService.register(request));
        verify(userRepository, never()).save(any(User.class));
    }

    @Test
    void shouldRegisterAdminWithCorrectRole() {
        RegisterRequest request = new RegisterRequest();
        request.setName("Админ");
        request.setEmail("admin@example.com");
        request.setPassword("admin123");

        when(userRepository.findByEmail(request.getEmail())).thenReturn(Optional.empty());
        when(passwordEncoder.encode(request.getPassword())).thenReturn("encoded_admin_pass");

        authService.registerAdmin(request);

        verify(userRepository, times(1)).save(argThat(user ->
                user.getRole() == UserRole.ROLE_ADMIN));
    }
}