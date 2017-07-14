/*
Navicat MySQL Data Transfer

Source Server         : Local_mysql
Source Server Version : 50627
Source Host           : localhost:3306
Source Database       : douban_group

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2017-07-13 11:31:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic_id` int(11) NOT NULL,
  `comment` varchar(700) COLLATE utf8mb4_unicode_ci NOT NULL,
  `release_time` datetime NOT NULL,
  `author` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for group_url
-- ----------------------------
DROP TABLE IF EXISTS `group_url`;
CREATE TABLE `group_url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `endpage` int(11) DEFAULT NULL,
  `pages` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lasttime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for picture
-- ----------------------------
DROP TABLE IF EXISTS `picture`;
CREATE TABLE `picture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) CHARACTER SET utf8 NOT NULL,
  `topic_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for topic
-- ----------------------------
DROP TABLE IF EXISTS `topic`;
CREATE TABLE `topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 NOT NULL,
  `author` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `comment_count` int(11) DEFAULT NULL,
  `comment_id_count` int(11) DEFAULT NULL,
  `comment_time_var` double DEFAULT NULL,
  `comment_distinct_count` int(11) DEFAULT NULL,
  `createtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `releasetime` datetime NOT NULL,
  `lasttime` datetime NOT NULL,
  `url` varchar(255) CHARACTER SET utf8 NOT NULL,
  `content_hash` bigint(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `content_hash` (`content_hash`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
DROP TRIGGER IF EXISTS `create_hash`;
DELIMITER ;;
CREATE TRIGGER `create_hash` BEFORE INSERT ON `topic` FOR EACH ROW BEGIN
SET NEW.content_hash=crc32( left(NEW.content,10)+right(NEW.content,10) );
END
;;
DELIMITER ;
