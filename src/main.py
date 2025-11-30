from typing import List
from sec_certs.dataset.fips import FIPSDataset
from sec_certs.sample.fips import FIPSCertificate
import glob
from pathlib import Path
# dset = FIPSDataset(root_dir="data/test_dataset")

dset: FIPSDataset = FIPSDataset()
# dset.root_dir = "data/test_dataset"
# dset.get_certs_from_web()

# certs: List[FIPSCertificate] = [dset2["0ab847ee0dd9fd88"]]

# dset = FIPSDataset()
# dset.root_dir = "data/test_dataset"
# dset.state.meta_sources_parsed = True
# dset.state.artifacts_downloaded = True


# dset.state.artifacts_downloaded = True

certs: List[FIPSCertificate] = []
for pdf_file in glob.glob("src/data/test_pdfs/*.pdf"):
    cert = FIPSCertificate(pdf_file, pdf_data=pdf_file)
    pdf_path = Path(pdf_file)
    cert.state.policy_download_ok = True
    cert.state.policy_convert_ok = False
    cert.state.policy_pdf_path = "src/data/test_pdfs/" + pdf_file.split("/")[-1]
    cert.state.policy_txt_path = "src/data/test_dataset/txt/"+ pdf_file.split("/")[-1].split(".")[0] + ".txt"
    cert.state._policy_json_path = "src/data/test_dataset/json/"+ pdf_path.name + ".json"
    certs.append(cert)

dset.update_with_certs(certs)
# dset.process_auxiliary_datasets()
# dset.download_all_artifacts()
# dset.convert_all_pdfs()
# dset.process_auxiliary_datasets(download_fresh=True)
# dset.analyze_certificates()
dset.extract_data()

print(len(dset.certs))
print(len(certs))
for cert in dset:
    print("==============================================")
    print("==============================================")
print("success")
