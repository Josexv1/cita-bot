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
        operation_code=OperationType.SOLICITUD_ASILO,
        doc_type=DocType.NIE,
        doc_value="Y0000000X",
        country="COUNTRY",
        name="Name Lastname",
        year_of_birth="1970",
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
#   python3 example_asilo.py
# or:
#   python3 example_asilo.py --autofill
