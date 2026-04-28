package com.anasttruh.spring_lab3_notifications.model.mapper;

import com.anasttruh.spring_lab3_notifications.model.dto.UserDto;
import com.anasttruh.spring_lab3_notifications.model.entity.User;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class UserMapper {

    public static UserDto toDto(User user) {
        if (user == null) return null;
        return UserDto.builder()
                .name(user.getName())
                .email(user.getEmail())
                .phone(user.getPhone())
                .telegramChatId(user.getTelegramChatId())
                .deviceToken(user.getDeviceToken())
                .createdAt(user.getCreatedAt())
                .build();
    }

    public static List<UserDto> toDtoList(List<User> users) {
        return users.stream().map(UserMapper::toDto).toList();
    }
}