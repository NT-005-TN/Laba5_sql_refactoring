package com.anasttruh.spring_lab3_notifications.service;

import com.anasttruh.spring_lab3_notifications.model.dto.NotificationDto;
import com.anasttruh.spring_lab3_notifications.model.entity.Notification;
import com.anasttruh.spring_lab3_notifications.model.entity.User;
import com.anasttruh.spring_lab3_notifications.model.enums.NotificationChannel;
import com.anasttruh.spring_lab3_notifications.model.enums.NotificationStatus;
import com.anasttruh.spring_lab3_notifications.repository.NotificationRepository;
import com.anasttruh.spring_lab3_notifications.repository.UserRepository;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
public class NotificationService {

    private final NotificationRepository notificationRepository;
    private final UserRepository userRepository;

    @Transactional
    public Notification createNotification(NotificationDto request) {
        User user = userRepository.findById(request.getRecipientId()).orElseThrow();

        Notification notification = new Notification();
        notification.setTitle(request.getTitle());
        notification.setMessage(request.getMessage());
        notification.setChannel(request.getChannel());
        notification.setStatus(NotificationStatus.CREATED);
        notification.setCreatedAt(LocalDateTime.now());
        notification.setRecipient(user);
        notificationRepository.save(notification);

//        if (true) {
//            throw new RuntimeException("Искусственная ошибка");
//        }

        return notification;
    }


        public List<Notification> getAllNotifications() {
        return notificationRepository.findAll();
    }

    public Notification getNotificationById(Long id) {
        return notificationRepository.findById(id).orElseThrow();
    }

    public Notification updateNotification(Long id, NotificationDto request)
    {
        Notification notification =
                notificationRepository.findById(id).orElseThrow();
        notification.setTitle(request.getTitle());
        notification.setMessage(request.getMessage());
        notification.setChannel(request.getChannel());
        notification.setStatus(request.getStatus());

        if (request.getStatus() == NotificationStatus.SENT) {
            notification.setSentAt(LocalDateTime.now());
        } else {
            notification.setSentAt(null);
        }

        return notificationRepository.save(notification);
    }

    public void deleteNotification(Long id) {
        Notification notification =
                notificationRepository.findById(id).orElseThrow();
        notificationRepository.delete(notification);
    }

    public List<Notification> getNotificationsByStatus(NotificationStatus status) {
        return notificationRepository.findByStatus(status);
    }

    public List<Notification> getNotificationsByChannel(NotificationChannel channel) {
        return notificationRepository.findByChannel(channel);
    }

    public List<Notification> getNotificationsByRecipientId(Long recipientId) {
        return notificationRepository.findByRecipientId(recipientId);
    }

}




















/*
public NotificationService(NotificationRepository notificationRepository) {
    this.notificationRepository = notificationRepository;
}
 */