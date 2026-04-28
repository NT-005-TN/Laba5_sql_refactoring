package com.anasttruh.spring_lab3_notifications.controller;

import com.anasttruh.spring_lab3_notifications.model.dto.UserDto;
import com.anasttruh.spring_lab3_notifications.model.mapper.UserMapper;
import com.anasttruh.spring_lab3_notifications.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @GetMapping("/all")
    public List<UserDto> getAllUsers() {
        // Используем новый маппер вместо ручного builder
        return UserMapper.toDtoList(userService.getAllUsers());
    }

    @GetMapping("/{id}")
    public UserDto getUserById(@PathVariable Long id) {
        // Используем новый маппер
        return UserMapper.toDto(userService.getUserById(id));
    }

    @PutMapping("/{id}")
    public UserDto updateUser(@PathVariable Long id, @RequestBody UserDto request) {
        // Используем новый маппер
        return UserMapper.toDto(userService.updateUser(id, request));
    }

    // Задание: Защита метода удаления через @PreAuthorize
    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public String deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return String.format("Пользователь %s удален", id);
    }
}