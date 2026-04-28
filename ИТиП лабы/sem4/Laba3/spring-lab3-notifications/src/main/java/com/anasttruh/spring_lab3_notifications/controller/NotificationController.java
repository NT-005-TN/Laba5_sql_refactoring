package com.anasttruh.spring_lab3_notifications.controller;

import com.anasttruh.spring_lab3_notifications.model.dto.NotificationDto;
import com.anasttruh.spring_lab3_notifications.model.entity.Notification;
import com.anasttruh.spring_lab3_notifications.model.enums.NotificationChannel;
import com.anasttruh.spring_lab3_notifications.model.enums.NotificationStatus;
import com.anasttruh.spring_lab3_notifications.model.mapper.NotificationMapper;
import com.anasttruh.spring_lab3_notifications.service.NotificationService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/notifications")
@RequiredArgsConstructor
public class NotificationController {

    private final NotificationService notificationService;

    @PostMapping("/add")
    public NotificationDto createNotification(@RequestBody @Valid NotificationDto request) {

        Notification response = notificationService.createNotification(request);
        return NotificationMapper.toDto(response);
    }

    @GetMapping("/all")
    public List<NotificationDto> getAllNotifications() {
        return NotificationMapper.toDtoList(notificationService.getAllNotifications());
    }

    @GetMapping("/{id}")
    public NotificationDto getNotificationById(@PathVariable Long id) {
        Notification response = notificationService.getNotificationById(id);
        return NotificationMapper.toDto(response);
    }

    @PutMapping("/{id}")
    public NotificationDto updateNotification(@PathVariable Long id, @RequestBody @Valid NotificationDto request) {
        Notification response = notificationService.updateNotification(id, request);

        return NotificationMapper.toDto(response);
    }

    @DeleteMapping("/{id}")
    public String deleteNotification(@PathVariable Long id) {
        notificationService.deleteNotification(id);
        return "Уведомление удалено";
    }

    @GetMapping("/status/{status}")
    public List<NotificationDto> getByStatus(@PathVariable NotificationStatus status) {
        return NotificationMapper.toDtoList(notificationService.getNotificationsByStatus(status));
    }

    @GetMapping("/channel/{channel}")
    public List<NotificationDto> getByChannel(@PathVariable NotificationChannel channel) {
        return NotificationMapper.toDtoList(notificationService.getNotificationsByChannel(channel));

    }

    @GetMapping("/recipient/{recipientId}")
    public List<NotificationDto> getByRecipientId(@PathVariable Long recipientId) {
        return NotificationMapper.toDtoList(notificationService.getNotificationsByRecipientId(recipientId));
    }
}
