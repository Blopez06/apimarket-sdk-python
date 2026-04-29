import pytest
from apimarket.validations import validate_curp, InvalidCURPError


class TestValidateCurp:
    @pytest.mark.parametrize("curp", [
        "LOOA531113HTCPBN07",
    ])
    def test_valid_curp(self, curp):
        assert validate_curp(curp) == curp

    @pytest.mark.skip(reason="Pending: need a real CURP whose check digit is 0")
    def test_curp_with_zero_check_digit_is_valid(self):
        # Covers the digit==10 branch in calculate_curp_verification_digit
        curp = "REEMPLAZAR_CON_CURP_REAL"
        assert validate_curp(curp) == curp

    @pytest.mark.parametrize("curp, expected_code, message_fragment", [
        ("LOOA531113",           InvalidCURPError.Code.INVALID_LENGTH, "18 caracteres"),
        ("LOOA531113HTCPBN07XX", InvalidCURPError.Code.INVALID_LENGTH, "18 caracteres"),
        ("123456789012345678",   InvalidCURPError.Code.INVALID_FORMAT, "formato"),
        ("LOOA531113HTCPBN09",   InvalidCURPError.Code.INVALID_DIGIT,  "Dígito verificador"),
    ])
    def test_invalid_curp(self, curp, expected_code, message_fragment):
        with pytest.raises(InvalidCURPError) as exc_info:
            validate_curp(curp)
        assert exc_info.value.code == expected_code
        assert message_fragment in exc_info.value.message

    def test_error_string_format(self):
        with pytest.raises(InvalidCURPError) as exc_info:
            validate_curp("LOOA531113")
        assert "INVALID_CURP_01" in str(exc_info.value)
