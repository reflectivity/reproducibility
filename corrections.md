# Corrections

This is a collaborative list of neutron and X-ray reflectometry corrections. 
Please be as detailed as possible when adding to it and where appropriate indicate radiation specificity. 

- Overspill correction: This accounts for when the beam footprint is greater than the sample size. [`islatu`](https://islatu.readthedocs.io) implements this as follows, 
    ```
    beam_sd = beam_width / 2 / np.sqrt(2 * np.log(2))
    length = sample_size * unp.sin(unp.radians(theta))
    mid = unp.nominal_values(length) / 2.0 / beam_sd
    upper = (unp.nominal_values(length) + unp.std_devs(length)) / 2.0 / beam_sd
    lower = (unp.nominal_values(length) - unp.std_devs(length)) / 2.0 / beam_sd
    probability = 2.0 * (
        unp.uarray(norm.cdf(mid), (norm.cdf(upper) - norm.cdf(lower)) / 2) - 0.5
    )
    reflectivity * probability
    ```
