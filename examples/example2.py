import os
import sys

from cita import CustomerProfile, DocType, Office, OperationType, Province, try_cita

if __name__ == "__main__":
    customer = CustomerProfile(
        anticaptcha_api_key="... your key here ...",
        auto_captcha=False,
        auto_office=True,
        chrome_driver_path="chromedriver",
        save_artifacts=True,
        province=Province.MADRID,
        operation_code=OperationType.TOMA_HUELLAS,
        min_date="21/04/2022",
        max_date="01/08/2022",
        doc_type=DocType.NIE,
        doc_value="Z0000000Y",
        country="COUNTRY",
        name="Name Lastname",
        year_of_birth="1980",
        phone="600123456",
        email="email@example.com",
        offices=[],
    )
    if "--autofill" not in sys.argv:
        try_cita(context=customer, cycles=200)  # Try 200 times
    else:
        from mako.template import Template

        tpl = Template(
            filename=os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "cita/template/autofill.mako"
            )
        )
        print(tpl.render(ctx=customer))  # Autofill for Chrome


# In Terminal run:
#   python3 example2.py
# or:
#   python3 example2.py --autofill
