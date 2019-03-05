/*
Navicat MySQL Data Transfer

Source Server         : zhiliao
Source Server Version : 50718
Source Host           : localhost:3306
Source Database       : orm_homework

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2018-04-12 20:00:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add article', '7', 'add_article');
INSERT INTO `auth_permission` VALUES ('20', 'Can change article', '7', 'change_article');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete article', '7', 'delete_article');
INSERT INTO `auth_permission` VALUES ('22', 'Can add category', '8', 'add_category');
INSERT INTO `auth_permission` VALUES ('23', 'Can change category', '8', 'change_category');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete category', '8', 'delete_category');
INSERT INTO `auth_permission` VALUES ('25', 'Can add author', '9', 'add_author');
INSERT INTO `auth_permission` VALUES ('26', 'Can change author', '9', 'change_author');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete author', '9', 'delete_author');
INSERT INTO `auth_permission` VALUES ('28', 'Can add tag', '10', 'add_tag');
INSERT INTO `auth_permission` VALUES ('29', 'Can change tag', '10', 'change_tag');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete tag', '10', 'delete_tag');
INSERT INTO `auth_permission` VALUES ('31', 'Can add student', '11', 'add_student');
INSERT INTO `auth_permission` VALUES ('32', 'Can change student', '11', 'change_student');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete student', '11', 'delete_student');
INSERT INTO `auth_permission` VALUES ('34', 'Can add course', '12', 'add_course');
INSERT INTO `auth_permission` VALUES ('35', 'Can change course', '12', 'change_course');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete course', '12', 'delete_course');
INSERT INTO `auth_permission` VALUES ('37', 'Can add score', '13', 'add_score');
INSERT INTO `auth_permission` VALUES ('38', 'Can change score', '13', 'change_score');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete score', '13', 'delete_score');
INSERT INTO `auth_permission` VALUES ('40', 'Can add teacher', '14', 'add_teacher');
INSERT INTO `auth_permission` VALUES ('41', 'Can change teacher', '14', 'change_teacher');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete teacher', '14', 'delete_teacher');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_teacher_id_b694c4f5_fk_teacher_id` (`teacher_id`),
  CONSTRAINT `course_teacher_id_b694c4f5_fk_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('1', 'Python', '1');
INSERT INTO `course` VALUES ('2', '前端', '2');
INSERT INTO `course` VALUES ('3', 'Java', '1');
INSERT INTO `course` VALUES ('4', '安卓', '3');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('7', 'front', 'article');
INSERT INTO `django_content_type` VALUES ('9', 'front', 'author');
INSERT INTO `django_content_type` VALUES ('8', 'front', 'category');
INSERT INTO `django_content_type` VALUES ('12', 'front', 'course');
INSERT INTO `django_content_type` VALUES ('13', 'front', 'score');
INSERT INTO `django_content_type` VALUES ('11', 'front', 'student');
INSERT INTO `django_content_type` VALUES ('10', 'front', 'tag');
INSERT INTO `django_content_type` VALUES ('14', 'front', 'teacher');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-03-29 06:29:41.797711');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-03-29 06:29:43.338023');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-03-29 06:29:43.702994');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-03-29 06:29:43.714023');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2018-03-29 06:29:43.920570');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2018-03-29 06:29:44.087050');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2018-03-29 06:29:44.219402');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2018-03-29 06:29:44.232399');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2018-03-29 06:29:44.346704');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2018-03-29 06:29:44.353783');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2018-03-29 06:29:44.368762');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2018-03-29 06:29:44.630460');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0009_alter_user_last_name_max_length', '2018-03-29 06:29:44.782864');
INSERT INTO `django_migrations` VALUES ('14', 'front', '0001_initial', '2018-03-29 06:29:45.306255');
INSERT INTO `django_migrations` VALUES ('15', 'sessions', '0001_initial', '2018-03-29 06:29:45.416550');
INSERT INTO `django_migrations` VALUES ('16', 'front', '0002_auto_20180329_1529', '2018-03-29 07:29:28.017217');
INSERT INTO `django_migrations` VALUES ('17', 'front', '0003_auto_20180330_2131', '2018-03-30 13:31:06.953309');
INSERT INTO `django_migrations` VALUES ('18', 'front', '0004_article_price', '2018-03-31 02:54:23.066603');
INSERT INTO `django_migrations` VALUES ('19', 'front', '0005_author', '2018-03-31 05:15:41.172177');
INSERT INTO `django_migrations` VALUES ('20', 'front', '0006_article_author', '2018-03-31 05:54:58.208085');
INSERT INTO `django_migrations` VALUES ('21', 'front', '0007_tag', '2018-04-01 11:14:53.602337');
INSERT INTO `django_migrations` VALUES ('22', 'front', '0008_auto_20180402_1743', '2018-04-02 09:43:55.204344');
INSERT INTO `django_migrations` VALUES ('23', 'front', '0009_auto_20180402_1745', '2018-04-02 09:45:49.331333');
INSERT INTO `django_migrations` VALUES ('24', 'front', '0010_article', '2018-04-04 02:20:07.909127');
INSERT INTO `django_migrations` VALUES ('25', 'front', '0011_auto_20180404_1533', '2018-04-04 07:33:38.552184');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for front_article
-- ----------------------------
DROP TABLE IF EXISTS `front_article`;
CREATE TABLE `front_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of front_article
-- ----------------------------
INSERT INTO `front_article` VALUES ('1', 'aaa', '2018-04-04 07:35:00.392356');

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` double NOT NULL,
  `course_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `score_course_id_9ac3760b_fk_course_id` (`course_id`),
  KEY `score_student_id_1b090b29_fk_student_id` (`student_id`),
  CONSTRAINT `score_course_id_9ac3760b_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`),
  CONSTRAINT `score_student_id_1b090b29_fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES ('1', '85', '1', '1');
INSERT INTO `score` VALUES ('2', '90', '2', '1');
INSERT INTO `score` VALUES ('3', '75', '3', '1');
INSERT INTO `score` VALUES ('5', '40', '1', '2');
INSERT INTO `score` VALUES ('6', '40', '2', '2');
INSERT INTO `score` VALUES ('7', '64', '3', '2');
INSERT INTO `score` VALUES ('8', '34', '4', '2');
INSERT INTO `score` VALUES ('9', '104', '1', '3');
INSERT INTO `score` VALUES ('10', '87', '2', '3');
INSERT INTO `score` VALUES ('11', '94', '3', '3');
INSERT INTO `score` VALUES ('12', '79', '4', '3');
INSERT INTO `score` VALUES ('13', '51', '1', '4');
INSERT INTO `score` VALUES ('14', '56', '2', '4');
INSERT INTO `score` VALUES ('15', '62', '3', '4');
INSERT INTO `score` VALUES ('16', '90', '4', '4');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `gender` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1', '张三', '1');
INSERT INTO `student` VALUES ('2', '李四', '2');
INSERT INTO `student` VALUES ('3', '王五', '1');
INSERT INTO `student` VALUES ('4', '赵六', '2');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('1', '黄老师');
INSERT INTO `teacher` VALUES ('2', '张老师');
INSERT INTO `teacher` VALUES ('3', '李老师');
