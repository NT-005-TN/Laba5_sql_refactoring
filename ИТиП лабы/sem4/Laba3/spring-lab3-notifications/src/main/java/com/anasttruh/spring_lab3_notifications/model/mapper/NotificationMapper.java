package com.anasttruh.spring_lab3_notifications.model.mapper;

import com.anasttruh.spring_lab3_notifications.model.dto.NotificationDto;
import com.anasttruh.spring_lab3_notifications.model.entity.Notification;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class NotificationMapper {
    public static NotificationDto toDto(Notification notification) {
        return NotificationDto.builder()
                .title(notification.getTitle())
                .message(notification.getMessage())
                .channel(notification.getChannel())
                .status(notification.getStatus())
                .createdAt(notification.getCreatedAt())
                .sentAt(notification.getSentAt())
                .recipientId(notification.getRecipient().getId())
                .build();
    }

    public static List<NotificationDto> toDtoList(List<Notification> notifications) {
        return notifications.stream().map(NotificationMapper::toDto).toList();
    }
}
