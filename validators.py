# validators.py - 数据验证模块

import re
from typing import Tuple


def validate_phone(phone: str) -> Tuple[bool, str]:
    """
    验证手机号格式
    返回 (是否有效, 错误消息)
    """
    if not phone or phone.strip() == "":
        return True, ""  # 手机号是可选的
    
    phone = phone.strip()
    
    # 中国大陆手机号验证
    pattern = r'^1[3-9]\d{9}$'
    if re.match(pattern, phone):
        return True, ""
    else:
        return False, "手机号格式不正确，请输入11位有效手机号（如：13800138000）"


def validate_password(password: str, min_length: int = 6) -> Tuple[bool, str]:
    """
    验证密码强度
    返回 (是否有效, 错误消息)
    """
    if not password:
        return False, "密码不能为空"
    
    if len(password) < min_length:
        return False, f"密码长度不能少于 {min_length} 位"
    
    # 可选：添加更强的密码要求
    # has_letter = any(c.isalpha() for c in password)
    # has_digit = any(c.isdigit() for c in password)
    # if not (has_letter and has_digit):
    #     return False, "密码需要包含字母和数字"
    
    return True, ""


def validate_required(value: str, field_name: str) -> Tuple[bool, str]:
    """
    验证必填字段
    返回 (是否有效, 错误消息)
    """
    if not value or value.strip() == "":
        return False, f"{field_name}不能为空"
    return True, ""


def validate_email(email: str) -> Tuple[bool, str]:
    """
    验证邮箱格式（备用）
    返回 (是否有效, 错误消息)
    """
    if not email or email.strip() == "":
        return True, ""  # 邮箱是可选的
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, ""
    else:
        return False, "邮箱格式不正确"
