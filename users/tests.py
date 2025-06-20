import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


# Test User Model Basics
@pytest.mark.django_db
def test_user_creation_with_roles():
    """Test that users can be created with roles (student/professor)."""
    student = User.objects.create_user(
        username="student1",
        password="testpass123",
        role="student"
    )
    professor = User.objects.create_user(
        username="prof1",
        password="testpass123",
        role="professor"
    )

    assert student.role == "student"
    assert professor.role == "professor"
    assert not student.is_superuser  # Default check


# Test Role Validation
@pytest.mark.django_db
def test_invalid_role_fails():
    """Test that invalid roles raise validation errors."""
    with pytest.raises(ValidationError):
        user = User(username="invalid", role="admin")  # Invalid role
        user.full_clean()  # Triggers validation


# Test Default Role
@pytest.mark.django_db
def test_default_role_is_student():
    """Ensure the default role is 'student' if not specified."""
    user = User.objects.create_user(username="defaultuser", password="test123")
    assert user.role == "student"  # As defined in your model