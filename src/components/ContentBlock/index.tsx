import { Row, Col } from "antd";
import { Fade } from "react-awesome-reveal";
import { useHistory } from 'react-router-dom';  // Import useHistory
import { withTranslation } from "react-i18next";

import { ContentBlockProps } from "./types";
import { Button } from "../../common/Button";
import { SvgIcon } from "../../common/SvgIcon";
import {
  ContentSection,
  Content,
  ContentWrapper,
  ServiceWrapper,
  MinTitle,
  MinPara,
  StyledRow,
  ButtonWrapper,
} from "./styles";

const ContentBlock = ({
  icon,
  title,
  content,
  section,
  button,
  t,
  id,
  direction,
}: ContentBlockProps) => {
  const history = useHistory();  // Initialize useHistory

  const handleNavigation = (path: string) => {
    history.push(path);
  };

  return (
    <ContentSection>
      <Fade direction={direction} triggerOnce>
        <StyledRow
          justify="space-between"
          align="middle"
          id={id}
          direction={direction}
        >
          <Col lg={11} md={11} sm={12} xs={24}>
            <SvgIcon src={icon} width="100%" height="100%" />
          </Col>
          <Col lg={11} md={11} sm={11} xs={24}>
            <ContentWrapper>
              <h6>{t(title)}</h6>
              <Content>{t(content)}</Content>
              {direction === "right" && (
                <ButtonWrapper>
                  {button && button.map((item, index) => (
                    <Button
                      key={index}
                      color={item.color}
                      onClick={() => handleNavigation('/new-page')}  // Update navigation path
                    >
                      {t(item.title)}
                    </Button>
                  ))}
                </ButtonWrapper>
              )}
            </ContentWrapper>
          </Col>
        </StyledRow>
      </Fade>
    </ContentSection>
  );
};

export default withTranslation()(ContentBlock);
